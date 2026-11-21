def binom(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r

def narayana(n, k):
    return binom(n, k) * binom(n, k - 1) // n

def gen(op, cl, n, s, out):
    if len(s) == 2 * n:
        out.append(s)
        return
    if op < n:
        gen(op + 1, cl, n, s + "(", out)
    if cl < op:
        gen(op, cl + 1, n, s + ")", out)

for n in range(1, 8):
    row = [narayana(n, k) for k in range(1, n + 1)]
    strings = []
    gen(0, 0, n, "", strings)
    by_peaks = [0] * (n + 1)
    for s in strings:
        by_peaks[s.count("()")] += 1
    agree = by_peaks[1:] == row
    print(f"n = {n}: {row} sum {sum(row)}, matches counted peaks: {str(agree).lower()}")
three = []
gen(0, 0, 3, "", three)
for s in three:
    print(f"{s} has {s.count('()')} peaks")
