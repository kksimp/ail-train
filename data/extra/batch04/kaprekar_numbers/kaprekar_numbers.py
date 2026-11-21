f = []
for n in range(1, 10000):
    sq = n * n; p = 10
    while p <= sq * 10:
        l, r = divmod(sq, p)
        if r > 0 and l + r == n: f.append(f"{n} ({sq} = {l}+{r})"); break
        p *= 10
print(f"{len(f)} Kaprekar numbers below 10000:")
for x in f: print(f"  {x}")
