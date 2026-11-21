import math
PI = 3.141592653589793

mass, disc_r, arm = 0.1, 0.03, 0.04
inertia = 0.5 * mass * disc_r * disc_r

def prec(w):
    return mass * 9.81 * arm / (inertia * w)

print(f"spin inertia {inertia * 10000000.0:.0f} g cm2")
w = 200.0
sec = 0
while True:
    p = prec(w)
    if p > w / 10.0:
        print(f"at {sec} s the spin {w:.1f} rad/s is too slow: precession {p:.2f} rad/s, the top topples")
        break
    if sec % 5 == 0:
        period = 2.0 * PI / p
        print(f"t {sec:>2} s: spin {w:>6.1f} rad/s, precession {p:.2f} rad/s, one turn every {period:.2f} s")
    w = w * 0.97
    sec += 1
