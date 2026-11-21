plants = [("mill stream", 0.5, 4.0, 0.6, 0.5), ("hill scheme", 2.0, 120.0, 0.85, 0.4), ("river dam", 300.0, 35.0, 0.88, 0.45), ("gorge dam", 900.0, 150.0, 0.92, 0.5)]
def megawatts(p):
    return p[3] * 1000.0 * 9.81 * p[1] * p[2] / 1000000.0
for p in plants:
    mw = megawatts(p)
    gwh = mw * 8760.0 * p[4] / 1000.0
    homes = int(gwh * 1000000.0 / 3500.0)
    print(f"{p[0]:<12} {p[1]:>6.1f} m3/s x {p[2]:>5.1f} m: {mw:>9.3f} MW, {gwh:>8.2f} GWh a year, {homes:>7} homes")
total = 0.0
for p in plants:
    total = total + megawatts(p)
print(f"all plants: {total:.1f} MW")
