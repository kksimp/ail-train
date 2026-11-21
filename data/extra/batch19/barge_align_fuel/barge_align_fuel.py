def fuel(pos, at, rising):
    t = 0
    for p in pos:
        d = abs(p - at)
        t += d * (d + 1) // 2 if rising else d
    return t

def best(pos, rising):
    w = min(pos)
    for at in range(min(pos), max(pos) + 1):
        if fuel(pos, at, rising) < fuel(pos, w, rising):
            w = at
    return [w, fuel(pos, w, rising)]

barges = [12, 3, 25, 7, 7, 18, 1, 30, 9, 14]
print(f"barges at {barges}")
a = best(barges, False)
print(f"part 1: moor at {a[0]} for {a[1]} fuel")
b = best(barges, True)
print(f"part 2: moor at {b[0]} for {b[1]} fuel")
print(f"for comparison, mooring 15 costs {fuel(barges, 15, False)} and {fuel(barges, 15, True)}")
