lines = [("Laptop", 1, 89900, 2100), ("Book", 3, 1595, 900), ("Cable", 2, 799, 2100), ("Bread", 4, 249, 900), ("Postage", 1, 495, 0)]
eur = lambda c: f"{c // 100}.{c % 100:02d}"
nb = {}
for t, q, u, r in lines:
    n = q * u; nb[r] = nb.get(r, 0) + n
    print(f"{t:<8}{q:>3} x {eur(u):>7} = {eur(n):>8}  {r // 100}%")
nt = vt = 0
for r in sorted(nb):
    n = nb[r]; v = (n * r + 5000) // 10000; nt += n; vt += v
    print(f"VAT {r // 100:>2}% on {eur(n):>8}: {eur(v):>7}")
print(f"net {eur(nt)}, VAT {eur(vt)}, total {eur(nt + vt)}")
