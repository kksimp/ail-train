from math import comb
def ball(n, r):
    return sum(comb(n, i) for i in range(r + 1))
def log2_floor(x):
    k = 0
    while (1 << (k + 1)) <= x:
        k += 1
    return k
print("  n  t  ball  upper words  lower words  data bits between")
for t in [1, 2, 3]:
    for n in [7, 15, 23]:
        up = (1 << n) // ball(n, t)
        lo = ((1 << n) + ball(n, 2 * t) - 1) // ball(n, 2 * t)
        perfect = "  perfect" if (1 << n) % ball(n, t) == 0 else ""
        print(f"{n:>3} {t:>2} {ball(n, t):>5} {up:>12} {lo:>12}  {log2_floor(lo)} to {log2_floor(up)}{perfect}")
print("perfect codes: Hamming (7,4) and (15,11) with t = 1, Golay (23,12) with t = 3")
