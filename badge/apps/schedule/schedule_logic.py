# Schedule logic for the GitHub Universe 2026 schedule app.
# Plain Python with no badge imports, so the same file runs on the badge
# (MicroPython) and on a desktop (CPython) via tools/validate_schedule.py.
# All times are whole minutes since 1970-01-01 in local venue time.
#
# bgateb - 20261026

import json
import math

PRE_ALERT_MIN = 10  # slow case-light pulse starts this long before a session
SOLID_MIN = 5       # case lights stay solid for the first X minutes of a session
APPROACH_MIN = 60   # the "next" progress bar fills over this amount of time (or the gap since the last session)
SLOT_MIN = 30       # one square per half hour in the day strip
DEFAULT_WALK = {"same_building": 5, "different_building": 10}

WEEKDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def days_from_civil(y, m, d):
    # Howard Hinnant's algorithm; avoids time.mktime, which differs between
    # CPython and MicroPython.
    if m <= 2:
        y -= 1
    era = y // 400
    yoe = y - era * 400
    mp = m - 3 if m > 2 else m + 9
    doy = (153 * mp + 2) // 5 + d - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe - 719468


def civil_from_days(z):
    z += 719468
    era = z // 146097
    doe = z - era * 146097
    yoe = (doe - doe // 1460 + doe // 36524 - doe // 146096) // 365
    doy = doe - (365 * yoe + yoe // 4 - yoe // 100)
    mp = (5 * doy + 2) // 153
    d = doy - (153 * mp + 2) // 5 + 1
    m = mp + 3 if mp < 10 else mp - 9
    y = yoe + era * 400 + (1 if m <= 2 else 0)
    return y, m, d


def to_minutes(y, m, d, hh=0, mm=0):
    return days_from_civil(y, m, d) * 1440 + hh * 60 + mm


def parse_day(text):
    parts = text.split("-") if isinstance(text, str) else ()
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        raise ValueError("bad day '%s' (want YYYY-MM-DD)" % text)
    y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
    if not (1 <= m <= 12 and 1 <= d <= 31):
        raise ValueError("bad day '%s' (want YYYY-MM-DD)" % text)
    return y, m, d


def parse_hm(text):
    parts = text.split(":") if isinstance(text, str) else ()
    if (len(parts) != 2 or not 1 <= len(parts[0]) <= 2 or len(parts[1]) != 2
            or not (parts[0].isdigit() and parts[1].isdigit())):
        raise ValueError("bad time '%s' (want HH:MM, 24-hour)" % text)
    h, m = int(parts[0]), int(parts[1])
    if h > 23 or m > 59:
        raise ValueError("bad time '%s' (want HH:MM, 24-hour)" % text)
    return h * 60 + m


def parse_stamp(text):
    # "2026-10-28 08:52" -> minutes
    parts = text.split(" ") if isinstance(text, str) else ()
    if len(parts) != 2:
        raise ValueError("bad time '%s' (want 'YYYY-MM-DD HH:MM')" % text)
    y, m, d = parse_day(parts[0])
    return to_minutes(y, m, d) + parse_hm(parts[1])


def load(text):
    """Parse schedule.json text. Raises ValueError with a readable message."""
    try:
        data = json.loads(text)
    except ValueError as e:
        raise ValueError("not valid JSON: %s" % e)
    if not isinstance(data, dict):
        raise ValueError("the file must be one JSON object {...}")

    walk = dict(DEFAULT_WALK)
    given = data.get("walk_minutes") or {}
    if not isinstance(given, dict):
        raise ValueError("walk_minutes must be an object")
    for key in walk:
        if key in given:
            value = given[key]
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError("walk_minutes.%s must be a whole number" % key)
            walk[key] = value

    rooms = data.get("rooms") or {}
    if not isinstance(rooms, dict):
        raise ValueError("rooms must be an object")

    raw = data.get("sessions")
    if not isinstance(raw, list) or not raw:
        raise ValueError("sessions must be a non-empty list")

    warnings = []
    sessions = []
    for n, s in enumerate(raw, 1):
        where = "session %d" % n
        if not isinstance(s, dict):
            raise ValueError(where + ": must be an object {...}")
        title = s.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(where + ": missing title")
        title = title.strip()
        where = "session %d (%s)" % (n, title[:30])
        for key in ("day", "start", "end"):
            if key not in s:
                raise ValueError("%s: missing %s" % (where, key))
        try:
            y, m, d = parse_day(s["day"])
            start = parse_hm(s["start"])
            end = parse_hm(s["end"])
        except ValueError as e:
            raise ValueError("%s: %s" % (where, e))
        if end <= start:
            raise ValueError("%s: end must be after start" % where)

        room = str(s.get("room") or "").strip()
        info = rooms.get(room) if room else None
        if room and not isinstance(info, dict):
            warnings.append("%s: room '%s' is not listed in rooms, so its building is unknown" % (where, room))
            info = None
        building = str((info or {}).get("building") or room)

        base = to_minutes(y, m, d)
        sessions.append({
            "n": n,
            "day": "%04d-%02d-%02d" % (y, m, d),
            "date_min": base,
            "start": base + start,
            "end": base + end,
            "title": title,
            "room": room,
            "building": building,
            "speaker": str(s.get("speaker") or "").strip(),
            "note": str(s.get("note") or "").strip(),
        })

    sessions.sort(key=lambda s: (s["start"], s["end"]))
    days = []
    for i, s in enumerate(sessions):
        s["i"] = i
        if s["day"] not in days:
            days.append(s["day"])

    debug_now = data.get("debug_now")
    if debug_now is not None:
        try:
            debug_now = parse_stamp(debug_now)
        except ValueError as e:
            raise ValueError("debug_now: %s" % e)
        warnings.append("debug_now is set; change it back to null before the event")

    return {
        "sessions": sessions,
        "days": days,
        "walk": walk,
        "debug_now": debug_now,
        "rtc_is_utc": bool(data.get("rtc_is_utc", False)),
        "warnings": warnings,
    }


def day_sessions(sched, day):
    return [s for s in sched["sessions"] if s["day"] == day]


def previous(sched, s):
    # The session before s on the same day, i.e. where you'd walk from.
    i = s["i"] - 1
    if i >= 0:
        p = sched["sessions"][i]
        if p["day"] == s["day"]:
            return p
    return None


def walk_hint(sched, s):
    """Walk from the previous session's building, or None if not needed."""
    prev = previous(sched, s)
    if (prev is None or not prev["building"] or not s["building"]
            or prev["building"] == s["building"]):
        return None
    walk = sched["walk"]["different_building"]
    leave_by = s["start"] - walk
    return {"from": prev, "walk": walk, "leave_by": leave_by,
            "tight": leave_by < prev["end"]}


def leave_by(sched, s):
    hint = walk_hint(sched, s)
    if hint:
        return hint["leave_by"]
    return s["start"] - sched["walk"]["same_building"]


def conflicts(sched):
    """List of ("overlap" | "tight", earlier, later) session pairs."""
    found = []
    sessions = sched["sessions"]
    for i, a in enumerate(sessions):
        for b in sessions[i + 1:]:
            if b["start"] >= a["end"]:
                break  # sorted by start, so nothing later overlaps a
            found.append(("overlap", a, b))
    for s in sessions:
        hint = walk_hint(sched, s)
        if hint and hint["tight"] and hint["from"]["end"] <= s["start"]:
            found.append(("tight", hint["from"], s))
    return found


def flagged(sched):
    """Indexes of sessions to mark in the day list."""
    marks = set()
    for kind, a, b in conflicts(sched):
        if kind == "overlap":
            marks.add(a["i"])
        marks.add(b["i"])
    return marks


def status(sched, now):
    cur = None
    nxt = None
    for s in sched["sessions"]:
        if s["start"] <= now < s["end"]:
            cur = s  # latest-starting wins when sessions overlap
        elif s["start"] > now and nxt is None:
            nxt = s
    return {"cur": cur, "nxt": nxt, "mode": alert_mode(sched, now, cur, nxt)}


def alert_mode(sched, now, cur, nxt):
    if cur is not None and now - cur["start"] < SOLID_MIN:
        return "solid"
    if nxt is not None:
        if now >= leave_by(sched, nxt):
            return "fast"
        if nxt["start"] - now <= PRE_ALERT_MIN:
            return "slow"
    return "off"


def progress(sched, cur, nxt, now_secs):
    """The countdown progress bar as (kind, fraction, leave_mark), or None.

    kind is "now" (current session elapsed), "next" (next session getting close)
    or "late" (past the leave-by time). leave_mark is where the leave-by time
    falls on the bar (0..1), or None when it isn't on this bar.
    """
    if cur is not None:
        begin, end = cur["start"] * 60, cur["end"] * 60
        kind, mark = "now", None
        if nxt is not None and nxt["day"] == cur["day"]:
            lb = leave_by(sched, nxt) * 60
            if begin < lb < end:
                mark = (lb - begin) / (end - begin)
                if now_secs >= lb:
                    kind = "late"
        return kind, (now_secs - begin) / (end - begin), mark
    if nxt is None:
        return None
    begin = nxt["start"] - APPROACH_MIN
    prev = previous(sched, nxt)
    if prev is not None and prev["end"] > begin:
        begin = prev["end"]
    begin, end = begin * 60, nxt["start"] * 60
    if end <= begin or now_secs < begin:
        return None
    lb = leave_by(sched, nxt) * 60
    mark = (lb - begin) / (end - begin) if begin < lb < end else None
    return ("late" if now_secs >= lb else "next"), (now_secs - begin) / (end - begin), mark


def day_strip(sched, day, now):
    """One day as contribution-graph cells, one per SLOT_MIN from the hour of the
    first session to the end of the last: (start, level, clash, past, current).
    level 0-4 is how much of the slot is booked, like GitHub's contribution levels."""
    sessions = day_sessions(sched, day)
    if not sessions:
        return []
    begin = sessions[0]["start"] // 60 * 60
    end = max(s["end"] for s in sessions)
    clash_spans = [(b["start"], min(a["end"], b["end"]))
                   for kind, a, b in conflicts(sched) if kind == "overlap" and a["day"] == day]
    cells = []
    t = begin
    while t < end:
        t2 = t + SLOT_MIN
        booked = 0
        for s in sessions:
            booked += max(0, min(s["end"], t2) - max(s["start"], t))
        booked = min(booked, SLOT_MIN)  # overlapping sessions don't count twice
        level = (booked * 4 + SLOT_MIN - 1) // SLOT_MIN
        clash = any(a < t2 and b > t for a, b in clash_spans)
        cells.append((t, level, clash, t2 <= now, t <= now < t2))
        t = t2
    return cells


def alert_level(mode, ticks):
    """Case-light brightness 0..1 for an alert mode at badge.ticks (ms)."""
    if mode == "solid":
        return 1.0
    if mode == "fast":
        return 0.5 + 0.5 * math.sin(ticks / 90)
    if mode == "slow":
        return 0.25 + 0.25 * math.sin(ticks / 500)
    return 0.0


def fmt_time(minutes):
    h = (minutes // 60) % 24
    suffix = "am" if h < 12 else "pm"
    return "%d:%02d%s" % (h % 12 or 12, minutes % 60, suffix)


def fmt_hour(minutes):
    # Short time for strip labels: "9a", "12p", "1:30p".
    h = (minutes // 60) % 24
    m = minutes % 60
    return "%d%s%s" % (h % 12 or 12, "" if m == 0 else ":%02d" % m, "a" if h < 12 else "p")


def fmt_day(minutes):
    days = minutes // 1440
    y, m, d = civil_from_days(days)
    return "%s %s %d" % (WEEKDAYS[(days + 3) % 7], MONTHS[m - 1], d)


def fmt_countdown(secs):
    if secs < 600:
        return "%d:%02d" % (secs // 60, secs % 60)
    mins = (secs + 59) // 60
    if mins < 60:
        return "%d min" % mins
    h, m = divmod(mins, 60)
    if h < 24:
        return "%dh %02dm" % (h, m)
    d, h = divmod(h, 24)
    return "%dd %dh" % (d, h)
