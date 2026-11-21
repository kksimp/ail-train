J = {3: 22, 8: 30, 28: 84, 58: 77, 75: 86, 80: 99, 17: 4, 52: 29, 57: 40, 62: 22, 88: 18, 95: 51, 97: 79}
R = [3, 5, 6, 2, 5, 4, 6, 6, 1, 3, 4, 2, 6, 5, 3, 3, 2, 4, 5, 1, 6, 6, 4, 2, 3, 5, 1, 2, 6, 4, 2, 3, 5, 6, 4, 1, 3, 2, 6, 5]
P = [0, 0]; t = 0; w = -1
for r in R:
    p = t % 2; g = P[p] + r
    if g <= 100:
        P[p] = g
        if g in J: print(f"player {p + 1} rolls {r}: {'ladder' if J[g] > g else 'snake'} {g} -> {J[g]}"); P[p] = J[g]
    if P[p] == 100: w = p; break
    t += 1
print(f"player {w + 1} wins after {t + 1} turns" if w >= 0 else f"no winner yet: {P[0]} and {P[1]}")
