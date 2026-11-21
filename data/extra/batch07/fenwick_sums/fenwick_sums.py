def ad(T, i, d):
    k = i + 1
    while k < len(T): T[k] += d; k += k & (-k)
def pf(T, i):
    s = 0; k = i + 1
    while k > 0: s += T[k]; k -= k & (-k)
    return s
S = [12, 7, 19, 4, 25, 8, 16, 3, 21, 10]; T = [0] * 11
for i, v in enumerate(S): ad(T, i, v)
for a, b in [(0, 4), (3, 7), (5, 9), (2, 2)]: print(f"days {a + 1}-{b + 1}: {pf(T, b) - (0 if a == 0 else pf(T, a - 1))} (plain {sum(S[a:b + 1])})")
ad(T, 4, -10); S[4] -= 10; print(f"after refund on day 5: days 1-10 = {pf(T, 9)} (plain {sum(S)})")
