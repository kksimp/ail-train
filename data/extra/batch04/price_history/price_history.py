P = [41, 38, 39, 45, 44, 47, 52, 50, 49, 55, 58, 54]; lo = P[0]; ld = 0; b = (0, 0, 0)
for i, p in enumerate(P):
    if p - lo > b[0]: b = (p - lo, ld, i)
    if p < lo: lo = p; ld = i
print(f"buy day {b[1] + 1}, sell day {b[2] + 1}, profit {b[0]}")
r = 1; L = 1
for i in range(1, len(P)):
    if P[i] > P[i - 1]: r += 1; L = max(L, r)
    else: r = 1
print(f"longest rise: {L} days")
print("moving average: " + " ".join(f"{sum(P[i:i + 3]) / 3:.1f}" for i in range(len(P) - 2)))
