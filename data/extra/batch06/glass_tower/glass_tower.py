for p in [1.0, 4.0, 7.0]:
    R = [[p]]
    for r in range(5):
        n = [0.0] * (r + 2)
        for i in range(r + 1):
            e = R[r][i] - 1.0
            if e > 0.0: n[i] += e / 2.0; n[i + 1] += e / 2.0; R[r][i] = 1.0
        R.append(n)
    print(f"poured {p:.0f} glasses:")
    for r in range(5): print(f"  row {r + 1}: {' '.join(f'{x * 100.0:.0f}%' for x in R[r])}")
