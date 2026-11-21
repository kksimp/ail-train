import math
def species(c, z, area):
    return c * area ** z
s1 = 18.0
a1 = 10.0
s2 = 58.0
a2 = 1000.0
z = math.log(s2 / s1) / math.log(a2 / a1)
c = s1 / a1 ** z
print(f"fitted z {z:.3f}, c {c:.2f}")
for area in [1.0, 50.0, 500.0, 5000.0, 20000.0]:
    print(f"island of {area:>7.1f} km2: about {species(c, z, area):.1f} species")
for lost in [50, 90, 99]:
    left = float(100 - lost) / 100.0
    kept = left ** z * 100.0
    print(f"lose {lost}% of the habitat, keep {kept:.1f}% of the species")
