import math
shields = [("lead", 1.2), ("steel", 2.1), ("concrete", 6.2), ("water", 18.0)]

def passes(hvl, cm):
    return math.pow(0.5, cm / hvl)

layers = math.log(100.0) / math.log(2.0)
print(f"cobalt-60 gamma rays; 1% needs {layers:.2f} half-value layers")
for name, hvl in shields:
    parts = [f"{passes(hvl, cm) * 100.0:.1f}%" for cm in [1.0, 5.0, 10.0]]
    print(f"{name:<9} HVL {hvl} cm: through 1, 5, 10 cm {' / '.join(parts)}; 1% at {hvl * layers:.1f} cm")
wall = passes(1.2, 5.0) * passes(6.2, 30.0)
print(f"5 cm lead plus 30 cm concrete passes {wall * 100.0:.3f}%")
