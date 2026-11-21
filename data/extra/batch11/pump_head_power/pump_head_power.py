duties = [("house tank", 0.8, 25.0, 0.55, 2.0), ("irrigation", 6.0, 12.0, 0.7, 6.0), ("borehole", 2.5, 60.0, 0.6, 4.0), ("fountain", 3.0, 1.5, 0.4, 10.0)]
def kw(d):
    head = d[2] * 1.1
    return 1000.0 * 9.81 * (d[1] / 1000.0) * head / d[3] / 1000.0
total = 0.0
for d in duties:
    k = kw(d)
    daily = k * d[4]
    total += daily
    print(f"{d[0]:<11} {d[1]} L/s up {d[2]} m: {k:.3f} kW, {daily:.2f} kWh a day")
cost = total * 30.0 * 0.25
print(f"all pumps: {total:.2f} kWh a day, {cost:.2f} a month at 0.25 per kWh")
