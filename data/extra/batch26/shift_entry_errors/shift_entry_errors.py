def minutes(t):
    p = t.split(":")
    if len(p) != 2: return None
    try:
        h, m = int(p[0]), int(p[1])
    except ValueError:
        return None
    if h > 23 or m > 59: return None
    return h * 60 + m
def shift(n, line):
    p = line.split(" ")
    if len(p) != 2: return (None, f"line {n}: expected a day and times")
    t = p[1].split("-")
    if len(t) != 2: return (None, f"line {n}: no dash in {p[1]}")
    a = minutes(t[0])
    if a is None: return (None, f"line {n}: bad start {t[0]}")
    b = minutes(t[1])
    if b is None: return (None, f"line {n}: bad end {t[1]}")
    if b <= a: return (None, f"line {n}: ends before it starts")
    return (b - a, None)
lines = ["Mon 09:00-17:30", "Tue 08:45-16:15", "Wed 9-17", "Thu 13:00-12:00", "Fri 07:30-15:45", "Sat", "Sun 10:00-25:00"]
total = 0; bad = []
for i, l in enumerate(lines):
    m, e = shift(i + 1, l)
    if e:
        print(f"skipped {e}"); bad.append(i + 1); continue
    total += m
    print(f"{l[0:3]}: {m // 60}h{m % 60:02}")
print(f"worked {total // 60}h{total % 60:02}, fix lines {bad}")
