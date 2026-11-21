import math
def vis_viva(mu, r, a): return math.sqrt(mu * (2.0 / r - 1.0 / a))
mu = 132712440018.0
au = 149597870.7
for name, a, e in [("Earth", 1.0, 0.0167), ("Mars", 1.524, 0.0934), ("Encke", 2.215, 0.8471), ("Halley", 17.834, 0.96714)]:
    q = a * (1.0 - e)
    big_q = a * (1.0 + e)
    vp = vis_viva(mu, q * au, a * au)
    va = vis_viva(mu, big_q * au, a * au)
    print(f"{name:<7} perihelion {q:>6.3f} AU at {vp:>5.2f} km/s, aphelion {big_q:>6.2f} AU at {va:>5.2f} km/s")
    print(f"        speed ratio {vp / va:.2f}, distance ratio {big_q / q:.2f}")
escape = vis_viva(mu, au, 1000000000000.0 * au)
print(f"leaving the Sun from 1 AU takes {escape:.1f} km/s")
