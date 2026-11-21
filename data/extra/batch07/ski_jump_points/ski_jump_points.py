def js(d, k, m): s = sorted(m); return 60.0 + (d - k) * 1.8 + s[1] + s[2] + s[3]
R = []
for n, d, m in [("Aho", 124.5, [18.0, 18.5, 17.5, 18.0, 19.0]), ("Berg", 131.0, [17.0, 17.5, 16.5, 17.5, 18.0]), ("Cruz", 117.5, [18.5, 19.0, 18.5, 19.5, 18.0]), ("Dahl", 109.0, [16.0, 15.5, 16.5, 16.0, 17.0])]:
    s = js(d, 120.0, m); R.append((n, s)); print(f"{n}: {d:.1f} m, {s:.1f} points")
print(f"winner {max(R, key=lambda r: r[1])[0]}")
