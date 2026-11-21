def gs(a, b):
    s = 0
    while b: a, b = b, a % b; s += 1
    return a, s
for a, b in [(1071, 462), (89, 55), (100, 75), (17, 5)]: g, s = gs(a, b); print(f"gcd({a}, {b}) = {g} in {s} steps")
print("    1 2 3 4 5 6 7 8")
for a in range(1, 9): print(f"{a:>2} " + "".join(" " + ("*" if gs(a, b)[0] == 1 else ".") for b in range(1, 9)))
l = 1
for n in range(1, 21): l = l // gs(l, n)[0] * n
print(f"lcm 1..20 = {l}")
