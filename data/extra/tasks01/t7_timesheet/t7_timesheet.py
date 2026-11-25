import sys

def digits(s, n):
    return len(s) == n and s.isascii() and s.isdigit()

def parse_time(s):
    p = s.split(":")
    if len(p) != 2 or not digits(p[0], 2) or not digits(p[1], 2):
        return None
    h, m = int(p[0]), int(p[1])
    if h > 23 or m > 59:
        return None
    return h * 60 + m

def valid_date(s):
    p = s.split("-")
    if len(p) != 3 or not digits(p[0], 4) or not digits(p[1], 2) or not digits(p[2], 2):
        return False
    return 1 <= int(p[1]) <= 12 and 1 <= int(p[2]) <= 31

mins = {}
days = {}
shifts = {}
seen = set()
for i, line in enumerate(sys.stdin.read().split("\n"), 1):
    line = line.rstrip("\r")
    if line.strip() == "":
        continue
    f = [x.strip() for x in line.split(",")]
    ok = len(f) == 4 and f[0] != "" and valid_date(f[1])
    if ok:
        a = parse_time(f[2])
        b = parse_time(f[3])
        ok = a is not None and b is not None and b > a
    if not ok:
        print(f"line {i}: invalid")
        continue
    paid = b - a
    if paid > 360:
        paid -= 30
    n = f[0]
    mins[n] = mins.get(n, 0) + paid
    shifts[n] = shifts.get(n, 0) + 1
    if (n, f[1]) not in seen:
        seen.add((n, f[1]))
        days[n] = days.get(n, 0) + 1

def hm(m):
    return f"{m // 60}:{m % 60:02d}"

for n in sorted(mins, key=lambda s: s.encode()):
    print(f"{n}: {hm(mins[n])} over {days[n]} days ({shifts[n]} shifts)")
print(f"all: {hm(sum(mins.values()))}")
