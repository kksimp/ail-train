def run(a12, a21):
    n1 = 50.0
    n2 = 40.0
    r1 = 0.8
    r2 = 0.6
    k1 = 1000.0
    k2 = 800.0
    dt = 0.1
    for _ in range(3000):
        d1 = r1 * n1 * (1.0 - (n1 + a12 * n2) / k1)
        d2 = r2 * n2 * (1.0 - (n2 + a21 * n1) / k2)
        n1 += d1 * dt
        n2 += d2 * dt
    return [n1, n2]

def verdict(n):
    if n[0] < 1.0 and n[1] < 1.0:
        return "both die out"
    elif n[1] < 1.0:
        return "species A wins"
    elif n[0] < 1.0:
        return "species B wins"
    return "they coexist"

print("A: r 0.8, K 1000; B: r 0.6, K 800; start 50 and 40")
for name, a12, a21 in [("weak rivalry", 0.5, 0.4), ("A pushes hard", 0.6, 1.5), ("B pushes hard", 1.6, 0.5), ("equal rivals", 1.0, 1.0)]:
    n = run(a12, a21)
    print(f"{name:<14} a12 {a12} a21 {a21}: A {n[0]:>6.1f}, B {n[1]:>6.1f}, {verdict(n)}")
a = (1000.0 - 0.5 * 800.0) / (1.0 - 0.5 * 0.4)
b = (800.0 - 0.4 * 1000.0) / (1.0 - 0.5 * 0.4)
print(f"weak rivalry equilibrium by hand: A {a:.1f}, B {b:.1f}")
