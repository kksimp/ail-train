from math import factorial
t = [factorial(i) for i in range(10)]
ds = lambda n: sum(t[int(c)] for c in str(n))
def cl(s):
    seen = set(); v = s
    while v not in seen: seen.add(v); v = ds(v)
    return len(seen)
print(f"0! to 9!: {t}")
print(f"equal to their digit factorial sum: {[n for n in range(10, 100000) if ds(n) == n]}")
for s in [69, 145, 169, 540, 871]: print(f"{s}: chain of {cl(s)}")
