import re
import sys
from datetime import date


def parse(s):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", s):
        return None
    y, m, d = int(s[:4]), int(s[5:7]), int(s[8:])
    if y < 1970 or y > 2100:
        return None
    try:
        return date(y, m, d)
    except ValueError:
        return None


def plural(k):
    return "1 day" if k == 1 else f"{k} days"


lines = sys.stdin.read().splitlines()
first = (lines[0] if lines else "").split(" ")
today = parse(first[1]) if len(first) == 2 and first[0] == "today" else None
if today is None:
    print("no today line")
    sys.exit(0)
open_tasks = []
done = 0
bad = []
for i in range(1, len(lines)):
    if lines[i].strip() == "":
        continue
    f = lines[i].split(" ", 2)
    d = parse(f[0]) if len(f) == 3 else None
    if d is None or f[1] not in ("open", "done") or f[2].strip() == "":
        bad.append(i + 1)
        continue
    if f[1] == "done":
        done += 1
    else:
        open_tasks.append((f[0], f[2], (d - today).days))
late = sorted([t for t in open_tasks if t[2] < 0], key=lambda t: (t[2], t[1].encode()))
soon = sorted([t for t in open_tasks if 0 <= t[2] <= 3], key=lambda t: (t[2], t[1].encode()))
print("OVERDUE")
if not late:
    print("  none")
for dt, name, days in late:
    print(f"  {plural(-days)}: {name} ({dt})")
print("DUE SOON")
if not soon:
    print("  none")
for dt, name, days in soon:
    label = "today" if days == 0 else plural(days)
    print(f"  {label}: {name} ({dt})")
print(f"done {done} open {len(open_tasks)} overdue {len(late)}")
for b in bad:
    print(f"bad line {b}")
