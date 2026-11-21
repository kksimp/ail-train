stages = [("inv", 1000.0, 10000.0), ("non", 1000.0, 4700.0), ("fol", 0.0, 0.0), ("inv", 2200.0, 1000.0)]
names = ["inverting x10", "non-inverting", "follower", "inverting /2.2"]
def gain(s):
    if s[0] == "inv":
        return 0.0 - s[2] / s[1]
    if s[0] == "non":
        return 1.0 + s[2] / s[1]
    return 1.0
def clip(v, rail):
    if v > rail:
        return rail
    if v < 0.0 - rail:
        return 0.0 - rail
    return v
for i, s in enumerate(stages):
    g = gain(s)
    outs = []
    for vin in [0.1, 0.5, 2.0]:
        v = clip(g * vin, 12.0)
        outs.append(f"{v:.2f}")
    joined = " ".join(outs)
    print(f"{names[i]:<15} gain {g:>6.2f}: {joined}")
