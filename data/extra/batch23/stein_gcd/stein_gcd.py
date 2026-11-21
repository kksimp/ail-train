def stein(a0, b0, steps):
    a = a0
    b = b0
    if a == 0 or b == 0:
        return a + b
    shift = 0
    while ((a | b) & 1) == 0:
        a = a >> 1
        b = b >> 1
        shift += 1
    while (a & 1) == 0:
        a = a >> 1
    while b != 0:
        while (b & 1) == 0:
            b = b >> 1
        if a > b:
            t = a
            a = b
            b = t
        b = b - a
        steps[0] += 1
    return a << shift

def euclid(a0, b0, steps):
    a = a0
    b = b0
    while b != 0:
        r = a % b
        a = b
        b = r
        steps[0] += 1
    return a

for pair in [[48, 18], [1071, 462], [270, 192], [1000000, 999999], [987, 610], [1024, 768], [0, 35]]:
    s1 = [0]
    s2 = [0]
    g1 = stein(pair[0], pair[1], s1)
    g2 = euclid(pair[0], pair[1], s2)
    print(f"gcd({pair[0]}, {pair[1]}) = {g1} (Euclid {g2}): {s1[0]} subtractions, {s2[0]} divisions")
