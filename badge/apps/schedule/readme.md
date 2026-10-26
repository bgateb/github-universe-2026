# Github Universe 2026 Badge App - Schedule Viewer

An offline schedule app for the GitHub Universe 2026 badge. It shows your next session with a live countdown, the room and building, and how long the walk is. When it's time to leave, it pulses the badge's case lights. Your sessions live in a `schedule.json` file on the badge, so the app works without Wi-Fi.

> **Status:** the app has been checked on a computer with the validator and the preview tool, but hasn't been run on a real badge yet.

## What it shows

**Now screen** (opens by default)
- The session you're in, with the time left and a pulsing green dot. Between sessions it shows the next one, with a countdown such as "in 12 min".
- The title, room and building, and speaker.
- A walk hint when the next session is in a different building from your previous one, for example "Leave by 10:52am • 8 min walk". It turns red when the gap is too short for the walk, and once it's time to leave.
- A bar under the countdown. It fills green during a session and gold over the last hour before your next one, then turns red once you're past the time to leave. A white tick marks when to leave.
- The session's note.
- A row of squares along the bottom, one per half hour of the day, shaded like a GitHub contribution graph by how much of that half hour is booked. Red squares are clashes.
- After your last session, "That's a wrap".

**Day list:** each day's sessions with time, title and room. The current session is green, the next one gold, and past ones dimmed. A ⚠ marks a clash or a walk you can't make in time.

**Detail:** the full title, speaker, room, the walk from the session before, any clash, and the full note.

**Case lights:**

| When | Lights |
| --- | --- |
| 10 minutes before your next session | slow pulse |
| Past the time you need to leave | fast pulse |
| First 5 minutes of a session | solid |
| Any other time | off |

The time to leave is the session's start minus the walk. The walk is `different_building` minutes if the session is in a different building from your previous one that day, otherwise `same_building` minutes.

## Controls

| Button | Now screen | Day list | Detail |
| --- | --- | --- | --- |
| B (tap) | Open the day list | Back to Now | Back to the day list |
| B (hold 2 seconds) | Set the clock | | |
| A | | Open details | Back to the day list |
| UP / DOWN | | Move through sessions | |
| LEFT / RIGHT | | Previous / next day | |

On the **Set clock** screen, UP / DOWN change the time by 1 minute and LEFT / RIGHT by 1 hour (hold to repeat). A adds a day, and B saves.

The badge's HOME button closes the app and turns the case lights off.

## Install

You need this `apps/schedule/` folder and `tools/validate_schedule.py` from the same repository. Run the commands below from the repository root.

### 1. Make your schedule

Start from the sample. It lists every room in the Universe session catalog and has one example session.

```bash
cp apps/schedule/schedule.json.sample apps/schedule/schedule.json
```

This replaces any `schedule.json` that's already there.

Then replace the example in `sessions` with your own picks:

```json
{"day": "2026-10-28", "start": "09:00", "end": "09:45",
 "title": "Opening Keynote", "room": "Main Stage",
 "speaker": "Cassidy Williams (GitHub)",
 "note": "New announcements, live demos and a few surprises."}
```

| Field | Required | Format |
| --- | --- | --- |
| `day` | yes | `YYYY-MM-DD` |
| `start`, `end` | yes | 24-hour `HH:MM` in venue time (Pacific). `end` must be later than `start` on the same day. |
| `title` | yes | Text |
| `room` | no | A name from `rooms`, exactly as written there. Use `""` if you don't know it yet. |
| `speaker` | no | Text |
| `note` | no | A short reminder, shown on the Now and Detail screens |

Sessions can be in any order; the app sorts them by start time. Overlapping sessions are allowed, and the app marks them as clashes.

**Picking the room.** The catalog shows each location as "Room @ Building", for example "Main Stage @ Festival Pavilion". Use the part before the "@" as `room`. A few rooms keep a floor or area in their name:

| Catalog location | `room` |
| --- | --- |
| Demos & Donuts @ Gateway Pavilion, Level 2 | `Demos & Donuts (Level 2)` |
| Workshops @ Gateway Pavilion, Level 1 | `Workshops (Level 1)` |
| The Speakeasy @ GitHub Central, Festival Pavilion | `The Speakeasy (GitHub Central)` |
| Sandbox @ Fort Mason Building C, Founders Inc., 3rd Floor | `Sandbox, 3rd Floor` |
| BATS Theatre @ Fort Mason Building B, 3rd Floor | `BATS Theatre, 3rd Floor` |

For a place that isn't in the catalog, such as a meeting room, add it to `rooms` with its building:

```json
"EC-1813": {"building": "GitHub Expert Center"}
```

Walk hints compare buildings, so rooms in the same building don't get one.

**Other settings** (the sample's values are fine for most people):

| Setting | Meaning |
| --- | --- |
| `walk_minutes` | Minutes to allow between sessions: `same_building` and `different_building`. Defaults are 5 and 10. |
| `rtc_is_utc` | Set to `true` if the badge clock runs on UTC rather than local time. See [How the clock works](#how-the-clock-works). |
| `debug_now` | `null` normally. For testing, a fake start time such as `"2026-10-28 08:52"`. |
| `_readme` | A note for people editing the file; the app ignores it. |

### 2. Check it

```bash
python3 tools/validate_schedule.py
```

This needs only Python 3, with no extra packages. It checks `apps/schedule/schedule.json`, then prints each day's agenda, any overlaps or walks you can't make in time, and warnings such as a room missing from `rooms`. It exits with an error if the badge couldn't load the file.

To see what the badge would show at a given time, add `--at` (you can repeat it):

```bash
python3 tools/validate_schedule.py --at "2026-10-28 10:45" --at "2026-10-29 08:00"
```

The validator uses the same `schedule_logic.py` as the badge, so a file that passes here will load on the badge.

### 3. Copy it to the badge

1. Plug the badge into your computer with USB-C.
2. On the badge's home menu, open **USB Disk**. The badge shows up on your computer as a drive, such as `/Volumes/BADGER` on macOS or `F:\` on Windows.
3. Copy three files into `apps/schedule/` on that drive: `__init__.py`, `schedule_logic.py` and `schedule.json`. The badge doesn't need the other files in this folder.

macOS or Linux (change the drive path to match yours):

```bash
mkdir -p /Volumes/BADGER/apps/schedule
# -X stops macOS adding "._" metadata files to the badge
cp -X apps/schedule/__init__.py apps/schedule/schedule_logic.py apps/schedule/schedule.json /Volumes/BADGER/apps/schedule/
```

On Linux, leave out `-X`.

Windows PowerShell (change `F:` to your drive letter):

```powershell
New-Item -ItemType Directory -Force F:\apps\schedule | Out-Null
Copy-Item .\apps\schedule\__init__.py, .\apps\schedule\schedule_logic.py, .\apps\schedule\schedule.json F:\apps\schedule\
```

4. Eject the drive. The badge restarts into MonaOS.

To update your schedule later, edit `schedule.json`, check it again, and copy only that file.

### 4. First run

Open the schedule app from the badge's home menu and check the time in the top right corner.

- If it says **Clock not set**, hold B for 2 seconds, set the time, and press B to save.
- If the time is wrong, hold B for 2 seconds on the Now screen to correct it.

## How it works

**Files on the badge**
- `__init__.py` is the MonaOS app: the screens, buttons and case lights.
- `schedule_logic.py` loads and checks `schedule.json` and works out the current and next sessions, walk hints, clashes, the progress bar, the day strip and the case-light timing. It doesn't use anything specific to the badge, so the same file runs on the badge (MicroPython) and in the computer tools (Python 3).
- `schedule.json` is your schedule. The app reads it from its own folder once, when it opens. If the file is missing or has a mistake, the app shows the problem on screen instead of crashing.

### How the clock works

The app reads the badge's clock as local time. It doesn't sync the time over Wi-Fi.

- **Corrections** you save on the Set clock screen are stored on the badge in `/state/schedule_clock.json`, as an offset from the badge clock, so they last until you change them.
- **A badge clock that has reset** (it reads earlier than 2026) shows the Clock not set screen. Saving then sets the badge clock itself.
- **A badge clock that runs on UTC:** set `"rtc_is_utc": true` in `schedule.json`. The app then adds `TIMEZONE` from `secrets.py` on the badge (hours from GMT, default `-7` for Pacific daylight time). [secrets.example.py](../../secrets.example.py) shows the format.
- **`debug_now`** replaces the real clock with a fake time that starts when the app opens and then ticks normally. Use it to see how a session looks without waiting for it. While it's set, the top bar shows a red **DEBUG** and clock corrections aren't saved. The validator warns until you set it back to `null`.

## Preview on a computer

`tools/badge_preview.py` runs the real app code on your computer and draws the screens with the Mona Sans font. It needs Pillow (`python3 -m pip install pillow`) and downloads the font on first run.

```bash
python3 tools/badge_preview.py                                    # mockups of every screen in preview/
python3 tools/badge_preview.py --live                             # a window you drive with the keyboard
python3 tools/badge_preview.py --live --at "2026-10-28 12:25"     # start at a given time
```

In the live window, the arrow keys are the d-pad, Z is A, and X is B (hold it for 2 seconds for the clock). `[` and `]` move the time back or forward 5 minutes, and `{` and `}` move it 1 hour. S saves a screenshot, and Q or Esc quits.

Text sizes are close to the badge's but not identical, so check final layouts on the device.

## Troubleshooting

| What you see | What to do |
| --- | --- |
| **schedule.json problem** on the badge | The message names the session and field. Fix it, run the validator, and copy the file again. |
| **Clock not set** | Hold B for 2 seconds and set the time. |
| Times off by exactly 7 hours | The badge clock runs on UTC. Set `"rtc_is_utc": true`. |
| Red **DEBUG** in the top bar | Set `debug_now` back to `null`. |
| A session shows no building, or a walk hint is missing | Its `room` isn't in `rooms`, or is spelled differently. The validator lists these. |

## Files in this repo

| File | Purpose | Copy to the badge? |
| --- | --- | --- |
| `__init__.py` | The badge app | yes |
| `schedule_logic.py` | Schedule logic shared with the computer tools | yes |
| `schedule.json.sample` | Sample Schedule json template with every catalog room pre-populated | no |

Related: [tools/validate_schedule.py](../../tools/validate_schedule.py)
