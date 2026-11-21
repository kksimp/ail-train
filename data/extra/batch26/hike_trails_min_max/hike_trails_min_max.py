trails = [("Ridge Loop", 124, 680), ("Lake Path", 58, 40), ("Fern Gully", 87, 310), ("Summit Push", 152, 1240), ("Mill Run", 43, 95)]
steep = lambda t: t[2] * 10 // t[1]
km = lambda t: f"{t[1] // 10}.{t[1] % 10} km"
long = max(trails, key=lambda t: t[1]); short = min(trails, key=lambda t: t[1])
st = max(trails, key=steep); ge = min(trails, key=steep)
print(f"longest   {long[0]}, {km(long)}")
print(f"shortest  {short[0]}, {km(short)}")
print(f"steepest  {st[0]}, {steep(st)} m/km")
print(f"gentlest  {ge[0]}, {steep(ge)} m/km")
for t in sorted([t for t in trails if t[1] <= 90 and steep(t) <= 40], key=lambda t: t[0]):
    print(f"family: {t[0]} {km(t)}, {t[2]} m up")
