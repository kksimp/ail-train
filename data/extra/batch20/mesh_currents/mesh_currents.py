def solve2(a, rhs):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    i1 = (rhs[0] * a[1][1] - a[0][1] * rhs[1]) / det
    i2 = (a[0][0] * rhs[1] - rhs[0] * a[1][0]) / det
    return [i1, i2]

e1 = 12.0
e2 = 6.0
r1 = 4.0
r2 = 2.0
r3 = 6.0
print(f"E1 {e1} V with R1 {r1} ohm, E2 {e2} V with R2 {r2} ohm, shared R3 {r3} ohm")
m = [[r1 + r3, -r3], [-r3, r2 + r3]]
cur = solve2(m, [e1, -e2])
i1 = cur[0]
i2 = cur[1]
shared = i1 - i2
print(f"loop currents: I1 {i1:.4f} A, I2 {i2:.4f} A")
print(f"through R3: {shared:.4f} A, R3 voltage {shared * r3:.4f} V")
supplied = e1 * i1 - e2 * i2
heat = r1 * i1 * i1 + r2 * i2 * i2 + r3 * shared * shared
print(f"batteries give {supplied:.4f} W, resistors take {heat:.4f} W")
d = "charging E2" if i2 < 0.0 else "draining E2"
print(f"the second battery is {d}")
