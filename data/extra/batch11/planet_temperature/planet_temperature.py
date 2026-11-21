import math
planets = [("Mercury", 0.387, 0.088, 440.0), ("Venus", 0.723, 0.76, 737.0), ("Earth", 1.0, 0.306, 288.0), ("Mars", 1.524, 0.25, 215.0), ("Jupiter", 5.2, 0.343, 165.0)]
def balance_k(p):
    return 278.6 * (1.0 - p[2]) ** 0.25 / math.sqrt(p[1])
for p in planets:
    t = balance_k(p)
    extra = p[3] - t
    print(f"{p[0]:<8} {p[1]:>5.3f} AU, albedo {p[2]:.3f}: {t:>5.1f} K ({t - 273.15:>6.1f} C), measured {p[3]} K, greenhouse {extra:>6.1f} K")
warmest = max(planets, key=lambda pl: int(pl[3] - balance_k(pl)))
print(f"biggest greenhouse effect: {warmest[0]}")
