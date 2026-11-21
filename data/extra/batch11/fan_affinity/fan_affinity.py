full_kw = 15.0
hours = 6000.0
price = 0.2
full_cost = full_kw * hours * price
print(f"full speed: {full_kw} kW, {full_cost:.1f} a year")
for pct in [90, 80, 70, 60, 50]:
    s = float(pct) / 100.0
    flow = s * 100.0
    pressure = s * s * 100.0
    kw = full_kw * s * s * s
    saving = (full_kw - kw) * hours * price
    print(f"{pct}% speed: flow {flow:.1f}%, pressure {pressure:.1f}%, power {kw:>6.3f} kW, saves {saving:>7.1f} a year")
target = 0.6
pct = 100
while full_kw * (float(pct) / 100.0) ** 3.0 > full_kw * target:
    pct -= 1
print(f"power under 60% of full from {pct}% speed")
