def sensible(kg, c, dt): return kg * c * dt
kg = 1.0
stages = [("warm ice -20 to 0 C", sensible(kg, 2.09, 20.0)), ("melt at 0 C", kg * 334.0), ("warm water 0 to 100 C", sensible(kg, 4.186, 100.0)), ("boil at 100 C", kg * 2257.0), ("warm steam 100 to 110 C", sensible(kg, 2.01, 10.0))]
total = 0.0
for s in stages: total = total + s[1]
running = 0.0
for name, kj in stages:
    running += kj
    pct = kj / total * 100.0
    secs = kj / 2.2
    print(f"{name:<24} {kj:>7.1f} kJ {pct:>5.1f}%  {secs:>6.0f} s on a 2.2 kW kettle")
print(f"total {total:.1f} kJ = {total / 3600.0:.3f} kWh")
lk = 0.0
for name, kj in stages:
    if name.startswith("melt") or name.startswith("boil"): lk = lk + kj
print(f"latent heat is {lk / total * 100.0:.1f}% of the energy")
