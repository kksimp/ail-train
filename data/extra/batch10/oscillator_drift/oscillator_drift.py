h = 0.1
ax, av = 1.0, 0.0
bx, bv = 1.0, 0.0
def energy(x, v):
    return (x * x + v * v) / 2.0
lo = hi = energy(bx, bv)
print(f"start energy {energy(ax, av):.4f}")
for step in range(1, 501):
    nx = ax + h * av
    nv = av - h * ax
    ax, av = nx, nv
    bv -= h * bx
    bx += h * bv
    e = energy(bx, bv)
    if e < lo:
        lo = e
    if e > hi:
        hi = e
    if step % 100 == 0:
        t = float(step) * h
        print(f"t {t:>4.0f}: explicit energy {energy(ax, av):>9.4f}, symplectic energy {e:.4f}")
print(f"symplectic energy stayed between {lo:.4f} and {hi:.4f}")
