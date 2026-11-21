s = w = g = 0
for c in range(3):
    for p in range(3):
        o = next(d for d in range(3) if d != c and d != p); ot = 3 - p - o; g += 1
        if p == c: s += 1
        if ot == c: w += 1
        print(f"car {c + 1}, pick {p + 1}, host opens {o + 1}, switch to {ot + 1}")
print(f"stick wins {s}/{g}, switch wins {w}/{g}")
