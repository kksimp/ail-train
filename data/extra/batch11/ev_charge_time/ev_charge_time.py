def power_at(soc, charger, car_max):
    base = charger if charger < car_max else car_max
    if soc < 80:
        return base
    return base * (1.0 - 0.9 * float(soc - 80) / 20.0)
def minutes(frm, upto, charger):
    step = 64.0 / 100.0
    total = 0.0
    for soc in range(frm, upto):
        total += step / power_at(soc, charger, 100.0) * 60.0
    return total
for name, kw in [("home 7 kW", 7.0), ("wallbox 11 kW", 11.0), ("rapid 50 kW", 50.0), ("ultra 150 kW", 150.0)]:
    to80 = minutes(10, 80, kw)
    to100 = minutes(10, 100, kw)
    print(f"{name:<14} 10-80%: {to80:>6.1f} min, 10-100%: {to100:>6.1f} min")
grid = 64.0 * 0.7 / 0.9
print(f"10-80% draws {grid:.2f} kWh from the grid, {grid * 0.3:.2f} at 0.30 per kWh")
