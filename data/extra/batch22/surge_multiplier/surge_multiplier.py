def mult(r, d):
    if d == 0:
        return 30
    ratio = r * 100 // d
    if ratio <= 100:
        return 10
    return min(10 + (ratio - 100) // 20, 30)

def money(c):
    return f"{c // 100}.{c % 100:02d}"

zones = [("harbour", 12, 15, 1450), ("station", 30, 18, 1200), ("stadium", 95, 20, 1600), ("airport", 9, 0, 3200), ("old town", 21, 14, 980)]
for name, r, d, base in zones:
    m = mult(r, d)
    fare = base * m // 10
    print(f"{name:<8} {r:>3} asking, {d:>2} free: x{m // 10}.{m % 10}, fare {money(fare)}")
busy = len([z for z in zones if mult(z[1], z[2]) > 10])
print(f"{busy} of {len(zones)} zones are surging")
