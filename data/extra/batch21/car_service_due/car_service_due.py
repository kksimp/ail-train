def ym(t):
    return f"{t // 12}-{t % 12 + 1:02d}"

def due(c, now):
    plate, last_month, last_km, km_now, per = c
    left = last_km + 15000 - km_now
    by_km = now if left <= 0 else now + left // per
    by_time = last_month + 12
    if by_km < by_time:
        return by_km, "distance"
    return by_time, "time"

now = 2026 * 12 + 10
cars = [("AB12 CDE", 2026 * 12 + 2, 41000, 50500, 1400), ("FG34 HIJ", 2025 * 12 + 11, 88000, 94000, 500), ("KL56 MNO", 2025 * 12 + 9, 12000, 19000, 700), ("PQ78 RST", 2026 * 12 + 5, 60000, 76000, 2000)]
print(f"today: {ym(now)}")
for c in cars:
    m, why = due(c, now)
    left = m - now
    if left <= 0:
        print(f"{c[0]}: OVERDUE by {why}")
    else:
        print(f"{c[0]}: due {ym(m)} by {why}, in {left} months")
order = sorted(cars, key=lambda c: due(c, now)[0])
print("booking order: " + ", ".join(c[0] for c in order))
