import math
PI = 3.141592653589793
def tan_phi(pf):
    return math.sqrt(1.0 - pf * pf) / pf
target = 0.95
for name, kw, pf in [("bakery", 40.0, 0.72), ("print shop", 26.0, 0.8), ("cold store", 60.0, 0.68), ("office", 15.0, 0.96)]:
    if pf >= target:
        print(f"{name:<11} pf {pf:.2f}: no correction needed")
        continue
    kvar = kw * (tan_phi(pf) - tan_phi(target))
    before = kw / pf
    after = kw / target
    micro = kvar * 1000.0 / (2.0 * PI * 50.0 * 400.0 * 400.0) * 1000000.0
    print(f"{name:<11} pf {pf:.2f}: add {kvar:>5.1f} kvar ({micro:.1f} uF at 400 V), {before:.1f} -> {after:.1f} kVA")
