# GitHub Universe 2026 Badge App - Schedule: offline next-session countdown with walk-time hints,
# a day list, per-session notes and a case-light alert before each talk.
# Sessions live in schedule.json next to this file; check edits on a computer
# with tools/validate_schedule.py (in the repo). See README.md for details.
#
# Controls: B (tap) Now <-> List, B (hold 2s) set clock, A open details,
# UP/DOWN move in the list, LEFT/RIGHT switch day. Screens slide between views.
# Also runs on a stock Tufty 2350 / the try.badgewa.re simulator, which has
# A, B, C, UP and DOWN only: C opens details and A is LEFT (see BTN_*).
#
# bgateb - 20261026

import json
import math
import os
import sys
import time

try:
    import machine
except ImportError:
    machine = None

try:
    import secrets
except ImportError:
    secrets = None

try:
    from badgeware import State  # saves to /state/<key>.json
except ImportError:
    State = None

APP_DIR = "/system/apps/schedule"
try:
    os.chdir(APP_DIR)  # badge app convention, so relative paths find our files
except OSError:
    pass  # e.g. the simulator, where this folder doesn't exist
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)
if "/" not in sys.path:
    sys.path.append("/")  # simulator uploads land in /

import schedule_logic as logic

badge.mode(HIRES | VSYNC)
screen.antialias = image.X2
try:
    import missing_details  # MonaOS (Universe badge)
    mona_sans = missing_details.mona_sans()
except ImportError:
    # Stock Badgeware and the simulator: load the same font directly.
    mona_sans = font.load("/system/assets/fonts/MonaSans-Medium.af")

# The 2026 Universe badge has a d-pad plus A (BUTTON_BACK) and B (BUTTON_SELECT).
# A stock Tufty has A, B, C, UP and DOWN: B selects, C opens details, A is LEFT
# (days wrap, so one direction reaches them all) and there is no RIGHT.
try:
    BTN_SELECT, BTN_OPEN, BTN_LEFT, BTN_RIGHT = BUTTON_SELECT, BUTTON_BACK, BUTTON_LEFT, BUTTON_RIGHT
    KEY_OPEN = "A"
except NameError:
    BTN_SELECT, BTN_OPEN, BTN_LEFT, BTN_RIGHT = BUTTON_B, BUTTON_C, BUTTON_A, None
    KEY_OPEN = "C"

BG       = color.rgb(10, 12, 20)
CARD     = color.rgb(32, 38, 58)
WHITE    = color.rgb(235, 245, 255)
CREAM    = color.rgb(248, 250, 244)
DIM      = color.rgb(140, 150, 170)
FAINT    = color.rgb(80, 88, 110)
PHOSPHOR = color.rgb(211, 250, 55)
GOLD     = color.rgb(249, 193, 110)
CYAN     = color.rgb(7, 157, 194)
RED      = color.rgb(235, 80, 80)

# Day strip: GitHub's dark-mode contribution greens, level 0 (free) to 4 (booked).
CONTRIB_RGB = ((22, 27, 34), (14, 68, 41), (0, 109, 50), (38, 166, 65), (57, 211, 83))
BG_RGB = (10, 12, 20)
LIVE_RGB = (211, 250, 55)  # PHOSPHOR


def mix(a, b, t):
    return color.rgb(int(a[0] + (b[0] - a[0]) * t), int(a[1] + (b[1] - a[1]) * t), int(a[2] + (b[2] - a[2]) * t))


CONTRIB = [color.rgb(*c) for c in CONTRIB_RGB]
CONTRIB_PAST = [mix(c, BG_RGB, 0.55) for c in CONTRIB_RGB]
CLASH_PAST = mix((235, 80, 80), BG_RGB, 0.55)

SCHEDULE_PATHS = (APP_DIR + "/schedule.json", "schedule.json", "/schedule.json")
CACHE_DIR = "/state"
CLOCK_FILE = CACHE_DIR + "/schedule_clock.json"

VIEW_NOW, VIEW_LIST, VIEW_DETAIL, VIEW_CLOCK = range(4)

HOLD_MS = 2000
REPEAT_DELAY_MS = 400
REPEAT_MS = 70

COUNTDOWN_Y = 36
BAR_X = 8
BAR_Y = 82
BAR_W = 304
BAR_H = 4
TITLE_Y = 88

SLIDE_MS = 180  # slide between screens; 0 turns it off
LIVE_MS = 1400  # pulse period of the live dot next to NOW

STRIP_Y = 227   # day strip along the bottom of the Now screen
STRIP_CELL = 9
STRIP_GAP = 2
NOTE_BOTTOM = STRIP_Y - 5

ICON_X = 8
ICON_TEXT_X = 24
ICON_MID = 0.76  # icon centre, as a fraction of text size below the text's y

LIST_TOP = 28
ROW_H = 38
LIST_ROWS = 5

try:
    os.mkdir(CACHE_DIR)
except OSError:
    pass


def file_exists_safe(p):
    try:
        os.stat(p)
        return True
    except OSError:
        return False


def load_schedule():
    for path in SCHEDULE_PATHS:
        if file_exists_safe(path):
            try:
                with open(path, "r") as f:
                    return logic.load(f.read()), None
            except ValueError as e:
                return None, str(e)
            except OSError as e:
                return None, "couldn't read %s: %s" % (path, e)
    return None, "schedule.json not found in apps/schedule/"


def setting_int(key, default):
    try:
        return int(getattr(secrets, key, default))
    except (TypeError, ValueError):
        return default


STATE_KEY = "schedule_clock"  # State writes /state/schedule_clock.json, the same as CLOCK_FILE


def load_offset():
    state = {"offset": 0}
    try:
        if State is not None:
            State.load(STATE_KEY, state)
        else:
            with open(CLOCK_FILE, "r") as f:
                state.update(json.load(f))
        return int(state.get("offset", 0))
    except (OSError, ValueError, AttributeError, TypeError):
        return 0


def save_offset(offset):
    try:
        if State is not None:
            State.save(STATE_KEY, {"offset": offset})
        else:
            with open(CLOCK_FILE, "w") as f:
                json.dump({"offset": offset}, f)
    except (OSError, ValueError, TypeError) as e:
        print("Schedule: couldn't save clock: %s" % e)


sched, load_error = load_schedule()
flags = logic.flagged(sched) if sched else set()
clashes = {}
for kind, a, b in (logic.conflicts(sched) if sched else ()):
    if kind == "overlap":
        clashes.setdefault(a["i"], []).append(b)
        clashes.setdefault(b["i"], []).append(a)
day_items = [logic.day_sessions(sched, d) for d in sched["days"]] if sched else []

# The clock is the badge RTC read as local time, plus TIMEZONE if the RTC runs
# on UTC, plus the correction saved from the set-clock screen. debug_now in
# schedule.json replaces all of that with a fake time that ticks from launch.
tz_adjust = setting_int("TIMEZONE", -7) * 3600 if sched and sched["rtc_is_utc"] else 0
clock_offset = load_offset()
start_ticks = badge.ticks
debug_base = sched["debug_now"] * 60 if sched and sched["debug_now"] is not None else None

# 1-bit icons drawn with rectangles in the current pen, so they take the colour
# of the text beside them. Built into (x, y, w, h) runs once at startup.
ICON_ROWS = {
    "clock": (
        "...#####...",
        ".##.....##.",
        ".#...#...#.",
        "#....#....#",
        "#....#....#",
        "#....####.#",
        "#.........#",
        "#.........#",
        ".#.......#.",
        ".##.....##.",
        "...#####...",
    ),
    "pin": (
        "...#####...",
        "..#######..",
        ".###...###.",
        ".##.....##.",
        ".##.....##.",
        ".###...###.",
        "..#######..",
        "...#####...",
        "....###....",
        "....###....",
        ".....#.....",
    ),
    "person": (
        "....###....",
        "...#####...",
        "...#####...",
        "...#####...",
        "....###....",
        "...........",
        "..#######..",
        ".#########.",
        "###########",
        "###########",
        "###########",
    ),
    "walk": (
        ".....##....",
        ".....##....",
        "...........",
        "....###....",
        "...#####...",
        "..#.###.#..",
        "..#.###..#.",
        "....#.#....",
        "...##.##...",
        "..##...##..",
        ".##.....##.",
    ),
    "dot": (
        "..###..",
        ".#####.",
        "#######",
        "#######",
        "#######",
        ".#####.",
        "..###..",
    ),
    "warn": (
        ".....#.....",
        "....###....",
        "....###....",
        "...##.##...",
        "...##.##...",
        "..###.###..",
        "..#######..",
        ".####.####.",
        "###########",
    ),
}


def icon_runs(rows):
    # Horizontal runs of "#", merged downwards when the next row repeats them.
    done = []
    open_runs = {}
    for y, row in enumerate(rows):
        runs = []
        x = 0
        while x < len(row):
            if row[x] == "#":
                start = x
                while x < len(row) and row[x] == "#":
                    x += 1
                runs.append((start, x - start))
            else:
                x += 1
        still_open = {}
        for run in runs:
            if run in open_runs:
                y0, h = open_runs.pop(run)
                still_open[run] = (y0, h + 1)
            else:
                still_open[run] = (y, 1)
        for (x0, w), (y0, h) in open_runs.items():
            done.append((x0, y0, w, h))
        open_runs = still_open
    for (x0, w), (y0, h) in open_runs.items():
        done.append((x0, y0, w, h))
    return (done, len(rows))


ICONS = {}
for _name in ICON_ROWS:
    ICONS[_name] = icon_runs(ICON_ROWS[_name])

view = VIEW_NOW
list_day = 0
cursor = 0
detail = None
edit_delta = 0
ox = 0             # x offset for put_text/put_rect while sliding
slide_from = None  # screen being slid away from: (view, list_day, cursor, detail)
slide_dir = 0      # +1: new screen comes in from the right, -1: from the left
slide_at = 0
repeat_at = {}
_fit_cache = {}
_strip = (None, None)  # (key, cells): the strip only changes once a minute


def rtc_secs():
    t = time.localtime()
    return logic.to_minutes(t[0], t[1], t[2], t[3], t[4]) * 60 + t[5]


def now_secs():
    if debug_base is not None:
        return debug_base + (badge.ticks - start_ticks) // 1000
    return rtc_secs() + tz_adjust + clock_offset


def year_of(secs):
    return logic.civil_from_days(secs // 86400)[0]


def set_rtc(secs):
    try:
        days = secs // 86400
        y, m, d = logic.civil_from_days(days)
        rem = secs % 86400
        machine.RTC().datetime((y, m, d, (days + 3) % 7, rem // 3600, rem // 60 % 60, rem % 60, 0))
        return True
    except Exception as e:
        print("Schedule: couldn't set RTC: %s" % e)
        return False


def save_clock():
    global clock_offset
    if debug_base is not None or edit_delta == 0:
        return
    desired = now_secs() + edit_delta
    # A badge clock that has reset (year before 2026) gets set directly, so the
    # saved correction doesn't depend on whatever it reset to.
    if time.localtime()[0] < 2026 and set_rtc(desired - tz_adjust):
        clock_offset = 0
    else:
        clock_offset += edit_delta
    save_offset(clock_offset)


def set_lights(level):
    try:
        badge.caselights(level)
    except Exception:
        pass


class Hold:
    """Tells a tap from a long hold on one button using badge.held()."""

    def __init__(self, button, hold_ms):
        self.button = button
        self.hold_ms = hold_ms
        self.down_at = None
        self.fired = False

    def update(self):
        # Returns "tap" (on release), "hold" (once, while held) or None.
        if held(self.button):
            if self.down_at is None:
                self.down_at = badge.ticks
                self.fired = False
            elif not self.fired and badge.ticks - self.down_at >= self.hold_ms:
                self.fired = True
                return "hold"
            return None
        was_down = self.down_at is not None
        self.down_at = None
        if was_down and not self.fired:
            return "tap"
        return None


def pressed(button):
    return button is not None and badge.pressed(button)


def held(button):
    return button is not None and badge.held(button)


b_button = Hold(BTN_SELECT, HOLD_MS)


def repeat(button):
    # True on press, then every REPEAT_MS once held past REPEAT_DELAY_MS.
    if pressed(button):
        repeat_at[button] = badge.ticks + REPEAT_DELAY_MS
        return True
    if held(button) and badge.ticks >= repeat_at.get(button, badge.ticks + 1):
        repeat_at[button] = badge.ticks + REPEAT_MS
        return True
    return False


_size_kw = False  # set if this firmware wants font_size= rather than a 4th argument


def put_text(text, x, y, size):
    global _size_kw
    if not _size_kw:
        try:
            screen.text(text, x + ox, y, size)
            return
        except TypeError:
            _size_kw = True
    screen.text(text, x + ox, y, font_size=size)


def put_rect(x, y, w, h):
    screen.rectangle(x + ox, y, w, h)


def draw_icon(name, x, y):
    runs, _ = ICONS[name]
    for dx, dy, w, h in runs:
        put_rect(x + dx, y + dy, w, h)


def icon_line(name, msg, y, size):
    """An icon then text, both in the current pen."""
    rows = ICONS[name][1]
    draw_icon(name, ICON_X, y + int(size * ICON_MID + 0.5) - rows // 2)
    put_text(fit(msg, 312 - ICON_TEXT_X, size), ICON_TEXT_X, y, size)


def text_w(text, size):
    return screen.measure_text(text, font_size=size)[0]


def fit(text, width, size):
    key = (text, width, size)
    if key not in _fit_cache:
        out = text
        if text_w(text, size) > width:
            while out and text_w(out + "...", size) > width:
                out = out[:-1]
            out = out.rstrip() + "..."
        _fit_cache[key] = out
    return _fit_cache[key]


def center_text(text, y, size):
    w, _ = screen.measure_text(text, font_size=size)
    if w > screen.width - 16:
        size = size * (screen.width - 16) / w
        w = screen.width - 16
    put_text(text, screen.width / 2 - w / 2, y, size)


def right_text(text, x_right, y, size):
    put_text(text, x_right - text_w(text, size), y, size)


def line_h(size):
    return int(size * 1.2 + 0.5)


def wrap(text, width, size, max_lines):
    # Word-wraps with measure_text instead of the firmware's rect wrapping, so
    # screens can flow and the last line ends in "..." when text doesn't fit.
    key = (text, width, size, max_lines)
    if key not in _fit_cache:
        lines = []
        line = ""
        for word in text.split():
            trial = word if not line else line + " " + word
            if not line or text_w(trial, size) <= width:
                line = trial
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
        if len(lines) > max_lines:
            lines = lines[:max_lines]
            last = lines[-1] if lines else ""
            while last and text_w(last + "...", size) > width:
                last = last[:-1]
            if lines:
                lines[-1] = last.rstrip() + "..."
        _fit_cache[key] = lines
    return _fit_cache[key]


def draw_wrapped(text, x, y, width, size, max_lines):
    """Draws word-wrapped text and returns the y below it."""
    lines = wrap(text, width, size, max_lines)
    for line in lines:
        put_text(line, x, y, size)
        y += line_h(size)
    return y


def lines_between(y, bottom, size):
    return max(0, (bottom - y - size) // line_h(size) + 1)


def where(s):
    if not s["room"]:
        return ""
    if s["building"] and s["building"] != s["room"]:
        return "%s  •  %s" % (s["room"], s["building"])
    return s["room"]


def focus_index(day_idx, st):
    items = day_items[day_idx]
    for s in (st["cur"], st["nxt"]):
        if s is not None and s["day"] == sched["days"][day_idx]:
            return items.index(s)
    return 0


def open_list(st, now):
    global view, list_day, cursor
    today = "%04d-%02d-%02d" % logic.civil_from_days(now // 86400)
    target = st["cur"] or st["nxt"]
    if today in sched["days"]:
        list_day = sched["days"].index(today)
    elif target is not None:
        list_day = sched["days"].index(target["day"])
    else:
        list_day = len(sched["days"]) - 1
    cursor = focus_index(list_day, st)
    view = VIEW_LIST


def open_clock(now, clock_ok):
    global view, edit_delta
    edit_delta = 0
    if not clock_ok:
        # Start from 8am on the first day rather than wherever the RTC reset to.
        edit_delta = (sched["sessions"][0]["date_min"] + 8 * 60) * 60 - now
    view = VIEW_CLOCK


def draw_top_bar(now):
    screen.pen = DIM
    put_text(logic.fmt_day(now // 60), 8, 4, 14)
    if debug_base is not None:
        screen.pen = RED
        right_text("DEBUG " + logic.fmt_time(now // 60), 312, 4, 14)
    else:
        screen.pen = WHITE
        right_text(logic.fmt_time(now // 60), 312, 4, 14)


def draw_walk(s, now, y):
    hint = logic.walk_hint(sched, s)
    if hint is None:
        return
    # The destination building is already on the room line above.
    if now // 60 >= hint["leave_by"]:
        screen.pen = RED
        msg = "Leave now  •  %d min walk" % hint["walk"]
    else:
        screen.pen = RED if hint["tight"] else GOLD
        msg = "%sLeave by %s  •  %d min walk" % (
            "Tight! " if hint["tight"] else "", logic.fmt_time(hint["leave_by"]), hint["walk"])
    icon_line("walk", msg, y, 14)


def draw_bar(bar):
    # Progress bar under the countdown; see logic.progress().
    if bar is None:
        return
    kind, frac, mark = bar
    frac = max(0.0, min(1.0, frac))
    screen.pen = CARD
    put_rect(BAR_X, BAR_Y, BAR_W, BAR_H)
    fill = int(BAR_W * frac)
    if fill > 0:
        screen.pen = RED if kind == "late" else (PHOSPHOR if kind == "now" else GOLD)
        put_rect(BAR_X, BAR_Y, fill, BAR_H)
    if mark is not None:
        screen.pen = WHITE  # leave-by tick
        put_rect(BAR_X + int(BAR_W * mark) - 1, BAR_Y - 2, 2, BAR_H + 4)


def draw_live_dot(x, y, size):
    # Pulses between dim and full brightness, next to text of this size at y.
    t = 0.5 + 0.5 * math.sin(badge.ticks * 2 * math.pi / LIVE_MS)
    screen.pen = mix(BG_RGB, LIVE_RGB, 0.3 + 0.7 * t)
    draw_icon("dot", x, y + int(size * ICON_MID + 0.5) - ICONS["dot"][1] // 2)


def strip_cells(day, now_min):
    global _strip
    key = (day, now_min)
    if _strip[0] != key:
        _strip = (key, logic.day_strip(sched, day, now_min))
    return _strip[1]


def draw_strip(day, now_min):
    """The day as a row of contribution squares, with start and end times."""
    cells = strip_cells(day, now_min)
    if not cells:
        return
    first = logic.fmt_hour(cells[0][0])
    last = logic.fmt_hour(cells[-1][0] + logic.SLOT_MIN)
    label_y = STRIP_Y + (STRIP_CELL + 1) // 2 - int(10 * ICON_MID + 0.5)
    screen.pen = DIM
    put_text(first, 8, label_y, 10)
    x = 8 + int(text_w(first, 10)) + 5
    room = 312 - int(text_w(last, 10)) - 5 - x
    cell = max(3, min(STRIP_CELL, (room + STRIP_GAP) // len(cells) - STRIP_GAP))
    for start, level, clash, past, current in cells:
        if current:
            screen.pen = WHITE
            put_rect(x - 1, STRIP_Y - 1, cell + 2, cell + 2)
        if clash:
            screen.pen = CLASH_PAST if past else RED
        else:
            screen.pen = (CONTRIB_PAST if past else CONTRIB)[level]
        put_rect(x, STRIP_Y, cell, cell)
        x += cell + STRIP_GAP
    screen.pen = DIM
    put_text(last, x + 3, label_y, 10)


def draw_focus(label, label_pen, countdown, s, bar, live=False):
    """Label, countdown, progress bar, title, room and speaker; returns the y below them."""
    screen.pen = label_pen
    put_text(label, 8, 26, 13)
    if live:
        draw_live_dot(8 + int(text_w(label, 13)) + 6, 26, 13)
        screen.pen = label_pen
    put_text(countdown, 8, COUNTDOWN_Y, 36)
    draw_bar(bar)
    screen.pen = WHITE
    y = draw_wrapped(s["title"], 8, TITLE_Y, 304, 19, 2) + 4
    screen.pen = CYAN
    if where(s):
        icon_line("pin", where(s), y, 15)
    else:
        icon_line("clock", logic.fmt_time(s["start"]), y, 15)
    y += 20
    if s["speaker"]:
        screen.pen = CREAM
        icon_line("person", s["speaker"], y, 14)
        y += 20
    return y


def draw_note(note, y, bottom, size):
    if note:
        screen.pen = DIM
        draw_wrapped(note, 8, y, 304, size, lines_between(y, bottom, size))


def draw_now(st, now):
    draw_top_bar(now)
    cur, nxt = st["cur"], st["nxt"]
    if cur is None and nxt is None:
        screen.pen = PHOSPHOR
        center_text("That's a wrap", 86, 32)
        screen.pen = DIM
        center_text("%d sessions over %d day%s" % (len(sched["sessions"]), len(sched["days"]), "" if len(sched["days"]) == 1 else "s"), 128, 15)
        center_text("B: list", 220, 12)
        return

    if cur is not None:
        y = draw_focus("NOW", PHOSPHOR, logic.fmt_countdown(cur["end"] * 60 - now) + " left", cur,
                       logic.progress(sched, cur, nxt, now), live=True)
        if nxt is not None and nxt["day"] == cur["day"]:
            screen.pen = DIM
            then = "Then %s  %s" % (logic.fmt_time(nxt["start"]), nxt["title"])
            icon_line("clock", then, y, 14)
            draw_walk(nxt, now, y + 20)
        else:
            draw_note(cur["note"], y + 2, NOTE_BOTTOM, 13)
        draw_strip(cur["day"], now // 60)
        return

    today = now // 86400
    if nxt["date_min"] // 1440 != today and logic.previous(sched, nxt) is None:
        label = "FIRST UP  •  " + logic.fmt_day(nxt["start"]).upper()
    else:
        label = "NEXT"
    y = draw_focus(label, GOLD, "in " + logic.fmt_countdown(nxt["start"] * 60 - now), nxt,
                   logic.progress(sched, None, nxt, now))
    if logic.walk_hint(sched, nxt) is not None:
        draw_walk(nxt, now, y)
        y += 20
    draw_note(nxt["note"], y + 2, NOTE_BOTTOM, 13)
    draw_strip(nxt["day"], now // 60)


def draw_list(st, now, day_idx, cur_idx):
    items = day_items[day_idx]
    screen.pen = WHITE
    put_text(logic.fmt_day(items[0]["date_min"]), 8, 4, 15)
    if len(day_items) > 1:
        screen.pen = DIM
        right_text("<  >", 312, 4, 15)

    first = max(0, min(cur_idx - 2, len(items) - LIST_ROWS))
    now_min = now // 60
    for row, s in enumerate(items[first:first + LIST_ROWS]):
        y = LIST_TOP + row * ROW_H
        if first + row == cur_idx:
            screen.pen = CARD
            put_rect(4, y, 312, ROW_H - 2)
        if s is st["cur"]:
            pen = PHOSPHOR
        elif s is st["nxt"]:
            pen = GOLD
        elif s["end"] <= now_min:
            pen = FAINT
        else:
            pen = WHITE
        screen.pen = pen
        put_text(logic.fmt_time(s["start"]), 10, y + 4, 13)
        put_text(fit(s["title"], 208, 15), 86, y + 3, 15)
        screen.pen = FAINT if pen is FAINT else DIM
        put_text(fit(where(s), 208, 12), 86, y + 21, 12)
        if s["i"] in flags:
            screen.pen = RED
            draw_icon("warn", 300, y + 12)

    screen.pen = DIM
    keys = KEY_OPEN + ": details   B: back"
    put_text(keys, 8, 224, 11)
    x = 8 + int(text_w(keys, 11)) + 14
    draw_icon("warn", x, 224 + int(11 * ICON_MID + 0.5) - ICONS["warn"][1] // 2)
    put_text("clash or tight walk", x + 15, 224, 11)


def draw_detail(s, now):
    draw_top_bar(now)
    screen.pen = GOLD
    icon_line("clock", "%s - %s" % (logic.fmt_time(s["start"]), logic.fmt_time(s["end"])), 26, 14)
    screen.pen = WHITE
    y = draw_wrapped(s["title"], 8, 46, 304, 19, 3) + 4
    if where(s):
        screen.pen = CYAN
        icon_line("pin", where(s), y, 15)
        y += 20
    if s["speaker"]:
        screen.pen = CREAM
        icon_line("person", s["speaker"], y, 14)
        y += 20
    hint = logic.walk_hint(sched, s)
    # Overlapping sessions get the "Clashes with" line below instead.
    if hint is not None and s["start"] >= hint["from"]["end"]:
        gap = s["start"] - hint["from"]["end"]
        if hint["tight"]:
            screen.pen = RED
            msg = "Tight: %d min gap, %d min walk from %s" % (gap, hint["walk"], hint["from"]["building"])
        else:
            screen.pen = GOLD
            msg = "%d min walk from %s" % (hint["walk"], hint["from"]["building"])
        icon_line("walk", msg, y, 14)
        y += 20
    for other in clashes.get(s["i"], ())[:1]:
        screen.pen = RED
        clash = "Clashes with %s  %s" % (logic.fmt_time(other["start"]), other["title"])
        icon_line("warn", clash, y, 14)
        y += 20
    draw_note(s["note"], y + 2, 222, 14)
    screen.pen = DIM
    put_text("B: back", 8, 224, 11)


def start_slide(direction):
    global slide_from, slide_dir, slide_at
    if SLIDE_MS:
        slide_from = (view, list_day, cursor, detail)
        slide_dir = direction
        slide_at = badge.ticks


def draw_screen(scene, st, now):
    v, day_idx, cur_idx, det = scene
    if v == VIEW_LIST:
        draw_list(st, now, day_idx, cur_idx)
    elif v == VIEW_DETAIL:
        draw_detail(det, now)
    else:
        draw_now(st, now)


def draw_clock(now):
    shown = now + edit_delta
    screen.pen = GOLD
    center_text("Set clock", 16, 24)
    screen.pen = WHITE
    center_text(logic.fmt_day(shown // 60), 64, 22)
    center_text(logic.fmt_time(shown // 60), 96, 48)
    screen.pen = DIM
    center_text("UP / DOWN   +/- 1 minute", 168, 14)
    if BTN_RIGHT is None:
        center_text("A   -1 hour", 186, 14)
    else:
        center_text("LEFT / RIGHT   +/- 1 hour", 186, 14)
    center_text(KEY_OPEN + "   +1 day        B   save", 204, 14)
    if debug_base is not None:
        screen.pen = RED
        center_text("debug_now is set, so changes won't be saved", 224, 12)


def draw_clock_prompt():
    screen.pen = RED
    center_text("Clock not set", 80, 28)
    screen.pen = WHITE
    center_text("Hold B for 2 seconds to set it", 124, 16)
    screen.pen = DIM
    center_text("The badge clock reads before 2026", 150, 13)


def draw_error(message):
    screen.pen = RED
    put_text("schedule.json problem", 8, 8, 20)
    screen.pen = WHITE
    draw_wrapped(message, 8, 40, 304, 15, 8)
    screen.pen = DIM
    draw_wrapped("Fix it over USB (check with tools/validate_schedule.py), then reopen the app.", 8, 196, 304, 12, 3)


def update():
    global view, list_day, cursor, detail, edit_delta, ox, slide_from

    screen.font = mona_sans
    screen.pen = BG
    screen.clear()

    if sched is None:
        set_lights(0)
        draw_error(load_error)
        return

    now = now_secs()
    clock_ok = debug_base is not None or year_of(now) >= 2026
    st = logic.status(sched, now // 60)
    b = b_button.update()

    if view == VIEW_NOW:
        if b == "hold":
            slide_from = None
            open_clock(now, clock_ok)
        elif b == "tap" and clock_ok:
            start_slide(1)
            open_list(st, now)
    elif view == VIEW_LIST:
        items = day_items[list_day]
        if pressed(BUTTON_UP):
            cursor = max(0, cursor - 1)
        elif pressed(BUTTON_DOWN):
            cursor = min(len(items) - 1, cursor + 1)
        elif (pressed(BTN_LEFT) or pressed(BTN_RIGHT)) and len(day_items) > 1:
            step = 1 if pressed(BTN_RIGHT) else -1
            start_slide(step)
            list_day = (list_day + step) % len(day_items)
            cursor = focus_index(list_day, st)
        elif pressed(BTN_OPEN):
            start_slide(1)
            detail = items[cursor]
            view = VIEW_DETAIL
        elif b == "tap":
            start_slide(-1)
            view = VIEW_NOW
    elif view == VIEW_DETAIL:
        if b == "tap" or pressed(BTN_OPEN):
            start_slide(-1)
            view = VIEW_LIST
    elif view == VIEW_CLOCK:
        if repeat(BUTTON_UP):
            edit_delta += 60
        if repeat(BUTTON_DOWN):
            edit_delta -= 60
        if repeat(BTN_RIGHT):
            edit_delta += 3600
        if repeat(BTN_LEFT):
            edit_delta -= 3600
        if pressed(BTN_OPEN):
            edit_delta += 86400
        if b == "tap":
            save_clock()
            edit_delta = 0
            view = VIEW_NOW
            now = now_secs()
            clock_ok = debug_base is not None or year_of(now) >= 2026
            st = logic.status(sched, now // 60)

    if view == VIEW_CLOCK:
        set_lights(0)
        draw_clock(now)
        return
    if not clock_ok:
        set_lights(0)
        draw_clock_prompt()
        return

    set_lights(logic.alert_level(st["mode"], badge.ticks))
    scene = (view, list_day, cursor, detail)
    if slide_from is not None:
        t = (badge.ticks - slide_at) / SLIDE_MS
        if t < 1:
            shift = int(screen.width * (1 - (1 - t) ** 3))  # ease out
            ox = -slide_dir * shift
            draw_screen(slide_from, st, now)
            ox = slide_dir * (screen.width - shift)
            draw_screen(scene, st, now)
            ox = 0
            return
        slide_from = None
    draw_screen(scene, st, now)


def on_exit():
    set_lights(0)


run(update)