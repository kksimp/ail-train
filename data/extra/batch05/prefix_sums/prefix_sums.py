S = [12, 30, 25, 8, 41, 37, 19, 22, 50, 14, 9, 33, 28, 46]; P = [0]
for s in S: P.append(P[-1] + s)
for a, b in [(0, 6), (3, 9), (7, 13), (5, 5)]: print(f"days {a + 1}-{b + 1}: {P[b + 1] - P[a]}")
b = 0; st = 0
for i in range(len(S) - 6):
    t = P[i + 7] - P[i]
    if t > b: b = t; st = i
print(f"best week: days {st + 1}-{st + 7}, {b}")
