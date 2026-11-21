def clock(q, j, k):
    return (j and not q) or (not k and q)

def value(f):
    v = 0
    for i in range(4):
        if f[i]:
            v += 1 << i
    return v

def show(f):
    return "".join("1" if f[i] else "0" for i in [3, 2, 1, 0])

def tick(f):
    q0, q1, q2, q3 = f
    f[0] = clock(f[0], True, True)
    f[1] = clock(f[1], q0 and not q3, q0 and not q3)
    f[2] = clock(f[2], q0 and q1, q0 and q1)
    f[3] = clock(f[3], q0 and q1 and q2, q0)

f = [False, False, False, False]
seen = []
for n in range(12):
    print(f"clock {n:>2}: {show(f)} = {value(f)}")
    seen.append(value(f))
    tick(f)
print(f"states visited before repeating: {seen[0:10]}")
