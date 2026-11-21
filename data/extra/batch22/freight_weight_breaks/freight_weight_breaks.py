def rate(w):
    return 4000 if w < 500 else (3200 if w < 1000 else (2500 if w < 2000 else 2000))

def money(c):
    return f"{c // 100}.{c % 100:02d}"

def best_charge(w):
    best = max(w * rate(w) // 100, 9500)
    billed = w
    for brk in [500, 1000, 2000]:
        if brk > w:
            c = brk * rate(brk) // 100
            if c < best:
                best = c
                billed = brk
    return best, billed

for w in [180, 350, 450, 820, 950, 1800, 1900, 2500]:
    actual = max(w * rate(w) // 100, 9500)
    charge, billed = best_charge(w)
    note = "" if billed == w else f" as {billed} lb"
    print(f"{w:>4} lb: actual {money(actual):>7}, charged {money(charge):>7}{note}")
