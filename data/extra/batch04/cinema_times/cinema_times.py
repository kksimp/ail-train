F = [("Tidewater", 112), ("Paper Moons", 95), ("The Long Field", 141)]; t = 720; cl = 23 * 60 + 30; i = 0; s = {f[0]: 0 for f in F}
c = lambda m: f"{m // 60:02}:{m % 60:02}"
while True:
    n, l = F[i % 3]
    if t + l > cl: break
    print(f"{c(t)}-{c(t + l)} {n}"); s[n] += 1; t += l + 20; i += 1
for f in F: print(f"{f[0]}: {s[f[0]]} shows")
