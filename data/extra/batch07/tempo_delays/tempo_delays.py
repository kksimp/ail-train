N = [("1/4", 1.0), ("1/8", 0.5), ("1/8 dotted", 0.75), ("1/8 triplet", 1.0 / 3.0), ("1/16", 0.25)]
for b in [90, 120, 140]:
    bt = 60000.0 / b; print(f"{b} bpm: " + ", ".join(f"{n} {bt * v:.1f}" for n, v in N) + " ms")
