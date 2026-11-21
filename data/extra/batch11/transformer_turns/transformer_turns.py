vp = 230.0
np_ = 2300
primary = 0.0
for name, turns, load in [("doorbell", 92, 4.0), ("lamp", 120, 6.0), ("charger", 500, 25.0)]:
    vs = vp * float(turns) / float(np_)
    amps = vs / load
    watts = vs * amps
    ip = watts / vp
    primary += ip
    print(f"{name:<9} {turns:>4} turns: {vs:>5.1f} V, {amps:.2f} A, {watts:>6.2f} W, primary {ip:.3f} A")
verdict = "fuse holds" if primary <= 0.5 else "fuse blows"
print(f"primary total {primary:.3f} A: {verdict}")
