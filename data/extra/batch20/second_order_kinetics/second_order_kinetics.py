import math

def conc2(a0, k, t):
    return 1.0 / (1.0 / a0 + k * t)

def conc1(a0, k1, t):
    return a0 * math.exp(-k1 * t)

k = 0.54
a0 = 0.1
first_half = 1.0 / (k * a0)
k1 = math.log(2.0) / first_half
print(f"2 NO2 -> 2 NO + O2, k {k} L/(mol s), [NO2]0 {a0} mol/L")
print(f"first half-life {first_half:.2f} s; first-order rival with the same half-life has k1 {k1:.5f} /s")
for t in [0.0, 10.0, 18.52, 50.0, 100.0, 300.0, 1000.0]:
    c2 = conc2(a0, k, t)
    c1 = conc1(a0, k1, t)
    print(f"t {t:>7.2f} s: second order {c2:.5f} mol/L, first order {c1:.5f} mol/L")
a = a0
halves = []
for _ in range(4):
    halves.append(f"{1.0 / (k * a):.1f}")
    a = a / 2.0
print(f"successive half-lives (s): {', '.join(halves)}")
