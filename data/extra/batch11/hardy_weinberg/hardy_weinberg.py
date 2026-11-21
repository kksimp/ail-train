import math
def carriers(incidence):
    q = math.sqrt(incidence)
    p = 1.0 - q
    return 2.0 * p * q
for label, n in [("1 in 2500", 2500), ("1 in 10000", 10000), ("1 in 400", 400)]:
    c = carriers(1.0 / float(n))
    print(f"condition {label}: carriers {c * 100.0:.2f}% (1 in {int(1.0 / c)})")
aa = 380
ab = 440
bb = 180
total = aa + ab + bb
p = float(2 * aa + ab) / float(2 * total)
q = 1.0 - p
expected = [p * p * float(total), 2.0 * p * q * float(total), q * q * float(total)]
observed = [aa, ab, bb]
chi = 0.0
for i in range(3):
    d = float(observed[i]) - expected[i]
    chi += d * d / expected[i]
print(f"observed [{aa}, {ab}, {bb}], p {p:.3f}, expected {expected[0]:.1f} {expected[1]:.1f} {expected[2]:.1f}")
verdict = "fits equilibrium" if chi < 3.84 else "departs from equilibrium"
print(f"chi-square {chi:.3f}: {verdict}")
