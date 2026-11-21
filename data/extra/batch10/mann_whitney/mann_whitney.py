import math

def ranks(values):
    order = sorted(range(len(values)), key=lambda i: int(values[i]))

    r = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        avg = float(i + j + 2) / 2.0
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r

coffee = [212.0, 198.0, 230.0, 205.0, 190.0, 221.0, 199.0, 205.0]
water = [240.0, 228.0, 251.0, 235.0, 219.0, 244.0, 230.0]
all_values = coffee + water
r = ranks(all_values)
n1, n2 = len(coffee), len(water)
r1 = 0.0
for i in range(n1):
    r1 += r[i]
u1 = r1 - float(n1 * (n1 + 1)) / 2.0
u2 = float(n1 * n2) - u1
mean = float(n1 * n2) / 2.0
sd = math.sqrt(float(n1 * n2 * (n1 + n2 + 1)) / 12.0)
z = (u1 - mean) / sd
print(f"ranks: {r}")
print(f"coffee rank sum {r1}, U1 = {u1}, U2 = {u2}")
print(f"mean U {mean}, sd {sd:.3f}, z = {z:.3f}")
verdict = "differ at the 5% level" if abs(z) > 1.96 else "no clear difference"
print(f"the groups {verdict}")
