import math
R = 8.314
F = 96485.0

def nernst_mv(z, inside, outside, t):
    return R * t / (float(z) * F) * math.log(outside / inside) * 1000.0

def goldman_mv(pk, pna, pcl, k, na, cl, t):
    top = pk * k[2] + pna * na[2] + pcl * cl[1]
    bottom = pk * k[1] + pna * na[1] + pcl * cl[2]
    return R * t / F * math.log(top / bottom) * 1000.0

t = 310.0
k = (1, 140.0, 5.0, "K+")
na = (1, 15.0, 145.0, "Na+")
cl = (-1, 10.0, 110.0, "Cl-")
for ion in [k, na, cl]:
    print(f"{ion[3]:<3} in {ion[1]:>5.1f} mM, out {ion[2]:>5.1f} mM: Nernst {nernst_mv(ion[0], ion[1], ion[2], t):>6.1f} mV")
rest = goldman_mv(1.0, 0.04, 0.45, k, na, cl, t)
spike = goldman_mv(1.0, 20.0, 0.45, k, na, cl, t)
print(f"resting (1 : 0.04 : 0.45): {rest:.1f} mV")
print(f"spike peak (1 : 20 : 0.45): {spike:.1f} mV")
high_k = (1, 140.0, 10.0, "K+")
print(f"doubling outside K+ moves rest to {goldman_mv(1.0, 0.04, 0.45, high_k, na, cl, t):.1f} mV")
