def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
a, b, c = (0, 0), (12, 0), (4, 9)
temps = [18.0, 24.0, 21.0]
whole = cross(a, b, c)
print(f"sensors at (0,0) 18 C, (12,0) 24 C, (4,9) 21 C; twice the area {whole}")
for p in [(4, 3), (6, 1), (0, 0), (8, 4), (10, 6)]:
    wa, wb, wc = cross(p, b, c), cross(a, p, c), cross(a, b, p)
    inside = wa >= 0 and wb >= 0 and wc >= 0
    t = (wa * temps[0] + wb * temps[1] + wc * temps[2]) / whole
    where = "inside" if inside else "outside"
    print(f"({p[0]},{p[1]}): weights {wa}/{whole} {wb}/{whole} {wc}/{whole}, {where}, blended {t:.2f} C")
