import math

def describe(f):
    if abs(f) < 0.0005:
        return "unloaded"
    return f"tension {f:.2f} kN" if f > 0.0 else f"compression {-f:.2f} kN"

def solve(span, cx, cy, fx, fy):
    rb = (fx * cy - fy * cx) / span
    ray = 0.0 - fy - rb
    rax = 0.0 - fx
    la = math.sqrt(cx * cx + cy * cy)
    lb = math.sqrt((span - cx) * (span - cx) + cy * cy)
    ux1 = -cx / la
    uy1 = -cy / la
    ux2 = (span - cx) / lb
    uy2 = -cy / lb
    det = ux1 * uy2 - ux2 * uy1
    f_ac = (-fx * uy2 + fy * ux2) / det
    f_bc = (-ux1 * fy + uy1 * fx) / det
    f_ab = -rax - f_ac * cx / la
    return [rax, ray, rb, f_ac, f_bc, f_ab]

for name, fx, fy in [("snow on the apex", 0.0, -12.0), ("wind from the left", 4.0, 0.0), ("snow and wind", 4.0, -12.0)]:
    r = solve(6.0, 2.0, 3.0, fx, fy)
    print(f"{name}: reactions A ({r[0]:.2f}, {r[1]:.2f}) kN, B {r[2]:.2f} kN")
    print(f"  AC {describe(r[3])}, BC {describe(r[4])}, AB {describe(r[5])}")
