import sys

lines = sys.stdin.read().splitlines()


def header():
    if len(lines) < 2:
        return None
    a = lines[0].split(" ")
    b = lines[1].split(" ")
    if len(a) != 2 or a[0] != "pattern" or a[1] == "" or any(c not in "DNO" for c in a[1]):
        return None
    if len(b) != 2 or b[0] != "days":
        return None
    t = b[1][1:] if b[1].startswith("-") else b[1]
    if not (t.isascii() and t.isdigit()):
        return None
    k = int(b[1])
    if k < 1 or k > 60:
        return None
    return a[1], k


h = header()
if h is None:
    print("bad header")
    sys.exit(0)
pat, days = h
people = []
rosters = []
for i in range(2, len(lines)):
    if lines[i].strip() == "":
        continue
    f = lines[i].split(" ")
    ok = len(f) == 2 and f[1].isascii() and f[1].isdigit()
    if not ok:
        print(f"bad line {i + 1}")
        continue
    off = int(f[1])
    r = "".join(pat[(d - 1 + off) % len(pat)] for d in range(1, days + 1))
    print(f"{f[0]} {r}")
    people.append(f[0])
    rosters.append(r)
for d in range(days):
    for shift in "DN":
        if not any(r[d] == shift for r in rosters):
            print(f"uncovered day {d + 1} shift {shift}")
for name, r in zip(people, rosters):
    print(f"worked {name} {sum(1 for c in r if c != 'O')}")
