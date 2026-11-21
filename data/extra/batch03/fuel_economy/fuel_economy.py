F = [(12000, 0.0), (12480, 34.2), (12910, 31.0), (13550, 41.6), (13880, 25.9), (14400, 35.1)]
L = []
for i in range(1, len(F)):
    km = F[i][0] - F[i - 1][0]; r = F[i][1] * 100.0 / km; L.append((km, r))
    print(f"leg {i}: {km} km, {F[i][1]} L, {r:.2f} L/100km")
tk = sum(l[0] for l in L); tl = sum(f[1] for f in F)
print(f"trip: {tk} km, {tl:.1f} L, {tl * 100.0 / tk:.2f} L/100km")
print(f"best {min(l[1] for l in L):.2f}, worst {max(l[1] for l in L):.2f}")
