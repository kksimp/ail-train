def quotient(n2, h2, nh3):
    return nh3 * nh3 / (n2 * h2 * h2 * h2)

def shift(q, k):
    r = q / k
    if abs(r - 1.0) < 0.01:
        return "Balanced"
    elif r < 1.0:
        return "Forward"
    return "Backward"

kc = 0.5
whats = {"Forward": "makes more ammonia", "Backward": "breaks ammonia down", "Balanced": "is at equilibrium"}
for n2, h2, nh3 in [(1.0, 1.0, 0.1), (0.5, 1.0, 0.5), (0.2, 0.3, 0.4), (2.0, 3.0, 4.0), (0.05, 0.1, 0.0)]:
    q = quotient(n2, h2, nh3)
    s = shift(q, kc)
    print(f"N2 {n2}, H2 {h2}, NH3 {nh3} mol/L: Q {q:.4f}, Shift.{s}, {whats[s]}")
rt = 0.08206 * 673.0
kp = kc / (rt * rt)
print(f"at 673 K, dn = -2 so Kp = {kp * 1000000.0:.3f} x 10^-6 per atm^2")
