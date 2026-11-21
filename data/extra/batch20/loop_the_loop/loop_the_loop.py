import math

def top(h, r):
    return 2.0 * 9.81 * (h - 2.0 * r)

def outcome(h, r):
    v2 = top(h, r)
    if v2 < 0.0:
        return "NoTop"
    elif v2 < 9.81 * r:
        return "Falls"
    return "Loops"

r = 4.0
m = 500.0
print(f"loop radius {r} m, lowest start height {2.5 * r} m")
msgs = {"NoTop": "cannot reach the top", "Falls": "reaches the top too slowly and falls", "Loops": "loops"}
for h in [7.0, 9.0, 10.5, 12.0, 16.0]:
    o = outcome(h, r)
    print(f"from {h} m: {msgs[o]}")
    if o == "Loops":
        v2 = top(h, r)
        n = m * (v2 / r - 9.81)
        print(f"  top speed {math.sqrt(v2):.2f} m/s, track pushes {n:.0f} N")
