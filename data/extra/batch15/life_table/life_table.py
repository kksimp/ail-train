ages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
qx = [0.006, 0.002, 0.007, 0.011, 0.022, 0.05, 0.11, 0.25, 0.55, 1.0]
lx = []; alive = 100000.0
for q in qx:
    lx.append(alive); alive = alive * (1.0 - q)
big_l = []
for i in range(len(lx)):
    nxt = lx[i + 1] if i + 1 < len(lx) else 0.0
    width = 10.0 if i + 1 < len(lx) else 5.0
    big_l.append((lx[i] + nxt) / 2.0 * width)
t = 0.0; ex = [0.0] * 10
for i in range(len(lx) - 1, -1, -1):
    t += big_l[i]; ex[i] = t / lx[i]
for k in range(len(ages)):
    dx = lx[k] * qx[k]
    print(f"age {ages[k]:>2}: lx {lx[k]:>8.0f}, dx {dx:>7.0f}, ex {ex[k]:>5.1f}")
print(f"chance a newborn reaches 80: {lx[8] / lx[0] * 100.0:.1f}%")
