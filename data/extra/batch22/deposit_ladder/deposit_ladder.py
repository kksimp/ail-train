def money(c):
    return f"{c // 100}.{c % 100:02d}"

def grow(v, bp):
    return v * (10000 + bp) // 10000

rates = [300, 340, 380, 410, 450]
rungs = [[200000, i + 1, rates[i]] for i in range(5)]
for year in range(1, 8):
    matured = []
    for r in rungs:
        r[0] = grow(r[0], r[2])
        r[1] -= 1
        if r[1] == 0:
            matured.append(money(r[0]))
            r[1] = 5
            r[2] = 450
    total = sum(r[0] for r in rungs)
    print(f"year {year}: matured {', '.join(matured)}, ladder worth {money(total)}")
avg = sum(r[2] for r in rungs) // len(rungs)
print(f"every deposit now earns {avg} basis points")
