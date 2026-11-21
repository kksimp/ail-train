import math

def tau(nm):
    r = 550.0 / nm
    return 0.1 * r * r * r * r

def kept(nm, m):
    return math.exp(-tau(nm) * m)

for name, nm in [("violet", 400.0), ("blue", 450.0), ("green", 530.0), ("yellow", 580.0), ("red", 680.0)]:
    ratio = tau(nm) / tau(680.0)
    noon = kept(nm, 1.0) * 100.0
    dusk = kept(nm, 38.0) * 100.0
    print(f"{name:<7} {nm:.0f} nm: scatters {ratio:.2f}x red, sun keeps {noon:.1f}% at noon, {dusk:.3f}% at sunset")
b = kept(450.0, 38.0)
r = kept(680.0, 38.0)
print(f"at sunset red outweighs blue {r / b:.0f} to 1")
