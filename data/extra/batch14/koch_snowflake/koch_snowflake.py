from math import gcd
sides, num, den, new_tris, tri_den = 3, 1, 1, 3, 9
print("step  sides  perimeter  area / first triangle")
for n in range(8):
    third = 1.0 / 3.0
    perim = 3.0 * (4.0 * third) ** float(n)
    g = gcd(num, den)
    ratio = num / den
    print(f"{n:>4} {sides:>6} {perim:>10.4f}  {num // g}/{den // g} = {ratio:.5f}")
    num = num * tri_den + new_tris * den
    den = den * tri_den
    g2 = gcd(num, den)
    num //= g2
    den //= g2
    sides *= 4
    new_tris *= 4
    tri_den *= 9
print("the area never passes 8/5 = 1.6 while the perimeter has no bound")
