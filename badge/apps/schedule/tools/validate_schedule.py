#!/usr/bin/env python3
"""Check apps/schedule/schedule.json and preview what the badge shows at given times.

Usage (from the repo root):
  python3 tools/validate_schedule.py
  python3 tools/validate_schedule.py --at "2026-10-28 10:45" --at "2026-10-29 08:00"
  python3 tools/validate_schedule.py path/to/other.json

Uses the same apps/schedule/schedule_logic.py the badge runs, so a file that
passes here loads on the badge. Exits 1 on errors; overlaps, tight walks and
warnings are printed but don't fail the check.
"""

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "apps", "schedule"))

import schedule_logic as logic  # noqa: E402


def span(s):
    return "%s-%s" % (logic.fmt_time(s["start"]), logic.fmt_time(s["end"]))


STRIP_CHARS = ".-=+#"  # contribution levels 0-4


def strip_text(sched, day, now):
    """The badge's day strip as text: one character per half hour, ! for a clash,
    and a ^ under the current half hour."""
    cells = logic.day_strip(sched, day, now)
    row = "".join("!" if clash else STRIP_CHARS[level] for _, level, clash, _, _ in cells)
    out = "%s %s %s" % (logic.fmt_hour(cells[0][0]), row, logic.fmt_hour(cells[-1][0] + logic.SLOT_MIN))
    marks = [i for i, cell in enumerate(cells) if cell[4]]
    if marks:
        out += "\n" + " " * (len(logic.fmt_hour(cells[0][0])) + 1 + marks[0]) + "^ now"
    return out


def print_agenda(sched, flags):
    for day in sched["days"]:
        sessions = logic.day_sessions(sched, day)
        print("\n%s   %s" % (logic.fmt_day(sessions[0]["date_min"]), strip_text(sched, day, 0)))
        for s in sessions:
            mark = "!" if s["i"] in flags else " "
            where = s["room"] if s["room"] == s["building"] else "%s, %s" % (s["room"], s["building"])
            print("  %s %-16s %-44s  %s" % (mark, span(s), s["title"][:44], where))


def print_issues(sched):
    issues = logic.conflicts(sched)
    if not issues:
        print("\nNo overlaps or tight walks.")
        return
    print()
    for kind, a, b in issues:
        if kind == "overlap":
            print("OVERLAP  %s %s overlaps %s %s" % (span(a), a["title"][:30], span(b), b["title"][:30]))
        else:
            gap = b["start"] - a["end"]
            print("TIGHT    %d min gap but %d min walk: %s (%s) -> %s (%s)" % (
                gap, sched["walk"]["different_building"],
                a["title"][:30], a["building"], b["title"][:30], b["building"]))


def describe(sched, stamp):
    now = logic.parse_stamp(stamp)
    st = logic.status(sched, now)
    cur, nxt = st["cur"], st["nxt"]
    print("\n@ %s %s" % (logic.fmt_day(now), logic.fmt_time(now)))
    if cur is None and nxt is None:
        print("  screen: That's a wrap")
    if cur is not None:
        print("  now:    %s  (%s left, %s)" % (cur["title"], logic.fmt_countdown((cur["end"] - now) * 60), cur["room"] or "no room"))
    if nxt is not None:
        print("  next:   %s %s  (in %s, %s)" % (
            logic.fmt_time(nxt["start"]), nxt["title"], logic.fmt_countdown((nxt["start"] - now) * 60), nxt["room"] or "no room"))
        hint = logic.walk_hint(sched, nxt)
        if hint:
            state = "LEAVE NOW" if now >= hint["leave_by"] else "leave by %s" % logic.fmt_time(hint["leave_by"])
            print("  walk:   %d min to %s, %s%s" % (hint["walk"], nxt["building"], state, " (tight)" if hint["tight"] else ""))
    bar = logic.progress(sched, cur, nxt, now * 60)
    if bar is not None:
        kind, frac, mark = bar
        print("  bar:    %d%% %s%s" % (max(0, min(100, frac * 100)), kind,
                                      "" if mark is None else ", leave-by tick at %d%%" % (mark * 100)))
    focus = cur or nxt
    if focus is not None:
        print("  strip:  " + strip_text(sched, focus["day"], now).replace("\n", "\n          "))
    print("  lights: %s" % st["mode"])


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", nargs="?", default=os.path.join(ROOT, "apps", "schedule", "schedule.json"))
    parser.add_argument("--at", action="append", default=[], metavar="'YYYY-MM-DD HH:MM'",
                        help="show what the badge would display at this local time (repeatable)")
    args = parser.parse_args()

    with open(args.path) as f:
        text = f.read()
    try:
        sched = logic.load(text)
        stamps = [(at, logic.parse_stamp(at)) for at in args.at]
    except ValueError as e:
        print("ERROR: %s" % e)
        return 1

    print("%s: %d sessions over %d day%s, OK" % (args.path, len(sched["sessions"]), len(sched["days"]), "" if len(sched["days"]) == 1 else "s"))
    print_agenda(sched, logic.flagged(sched))
    print_issues(sched)
    for warning in sched["warnings"]:
        print("WARNING  %s" % warning)
    for at, _ in stamps:
        describe(sched, at)
    return 0


if __name__ == "__main__":
    sys.exit(main())
