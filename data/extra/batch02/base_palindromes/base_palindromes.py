def dg(n, b):
    if n == 0: return [0]
    o = []
    while n: o.append(n % b); n //= b
    return o[::-1]
p = lambda d: d == d[::-1]
both = [n for n in range(1, 1000) if p(dg(n, 10)) and p(dg(n, 2))]
for n in both: print(f"{n:>4} = {''.join(map(str, dg(n, 2)))}")
print(f"sum: {sum(both)}")
for b in [3, 8, 16]: print(f"base {b} palindromes below 1000: {sum(1 for n in range(1, 1000) if p(dg(n, b)))}")
