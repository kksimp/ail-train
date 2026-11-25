import sys

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]


def toint(s):
    t = s[1:] if s.startswith("-") else s
    return int(s) if t.isascii() and t.isdigit() else None


meets = {}
enrols = []
seen = set()
for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line.strip() == "":
        continue
    f = line.split(" ")
    if len(f) == 5 and f[0] == "meet":
        s, e = toint(f[3]), toint(f[4])
        if f[2] not in DAYS or s is None or e is None or s >= e:
            print(f"bad line {n}")
            continue
        meets.setdefault(f[1], []).append((DAYS.index(f[2]), s, e))
    elif len(f) == 3 and f[0] == "enrol":
        if (f[1], f[2]) not in seen:
            seen.add((f[1], f[2]))
            enrols.append((f[1], f[2]))
    else:
        print(f"bad line {n}")
by_student = {}
for st, c in enrols:
    if c in meets:
        by_student.setdefault(st, []).append(c)
    else:
        print(f"unknown course {c} for {st}")
count = 0
for st in sorted(by_student, key=lambda s: s.encode()):
    cs = sorted(by_student[st], key=lambda s: s.encode())
    for i in range(len(cs)):
        for j in range(i + 1, len(cs)):
            days = [
                x[0]
                for x in meets[cs[i]]
                for y in meets[cs[j]]
                if x[0] == y[0] and x[1] < y[2] and y[1] < x[2]
            ]
            if days:
                print(f"{st}: {cs[i]} clashes with {cs[j]} on {DAYS[min(days)]}")
                count += 1
print(f"clashes {count}")
