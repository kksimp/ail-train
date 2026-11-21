def band(h): return "night" if h <= 6 or h == 23 else "peak" if 17 <= h <= 20 else "day"
R = {"night": 12, "peak": 41, "day": 24}
u = [3, 2, 2, 2, 2, 3, 5, 9, 7, 5, 4, 4, 5, 4, 4, 5, 7, 12, 14, 13, 10, 8, 6, 4]
cost, kwh = {}, {}
for h, x in enumerate(u):
    b = band(h); cost[b] = cost.get(b, 0) + x * R[b]; kwh[b] = kwh.get(b, 0) + x
for b in ["night", "day", "peak"]:
    print(f"{b:<6} {kwh.get(b, 0):>3} kWh  {cost.get(b, 0):>5}c")
t = sum(cost.values())
print(f"total {t // 100}.{t % 100:02d}")
f = sum(u) * 24
print(f"on a flat 24c rate: {f // 100}.{f % 100:02d}")
print("night hours: " + ",".join(str(h) for h in range(24) if band(h) == "night"))
