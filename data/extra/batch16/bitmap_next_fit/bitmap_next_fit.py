def used(m, i):
    return (m >> i) & 1 == 1

def picture(m):
    return " ".join("".join("#" if used(m, i) else "." for i in range(g * 10, g * 10 + 10)) for g in range(4))

def find_run(m, n, frm):
    for k in range(40):
        start = (frm + k) % 40
        if start + n <= 40:
            if all(not used(m, i) for i in range(start, start + n)):
                return start
    return -1

m = 0
for b in [0, 1, 2, 3, 10, 11, 12, 20, 25, 26, 27]:
    m |= 1 << b
print(f"start      {picture(m)}")
cursor = 0
where = {}
reqs = [("a", 5), ("b", 3), ("c", 6), ("a", -5), ("d", 4), ("e", 8), ("f", 2)]
for name, n in reqs:
    if n < 0:
        s = where[name]
        for i in range(s, s - n):
            m &= ~(1 << i)
        print(f"free {name}     {picture(m)}")
        continue
    s = find_run(m, n, cursor)
    if s < 0:
        print(f"{name} x{n}: no run of {n} free blocks")
        continue
    for i in range(s, s + n):
        m |= 1 << i
    where[name] = s
    cursor = s + n
    print(f"{name} x{n} @{s:<2}  {picture(m)}")
