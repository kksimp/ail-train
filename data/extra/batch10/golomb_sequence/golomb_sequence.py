import math

def golomb(count):
    a = [0, 1]
    for n in range(2, count + 1):
        a.append(1 + a[n - a[a[n - 1]]])
    return a

a = golomb(10000)
print(f"a(1..30) = {a[1:31]}")
ok = True
for v in range(1, 21):
    if a[1:].count(v) != a[v]:
        ok = False
print(f"each of 1..20 appears a(n) times: {str(ok).lower()}")
phi = (1.0 + math.sqrt(5.0)) / 2.0
for n in [10, 100, 1000, 10000]:
    nf = float(n)
    est = math.pow(phi, 2.0 - phi) * math.pow(nf, phi - 1.0)
    print(f"a({n}) = {a[n]}, estimate {est:.1f}")
