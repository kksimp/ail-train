def steps(cr, ci, lim):
    zr = zi = 0.0
    for k in range(lim):
        if zr * zr + zi * zi > 4.0: return k
        t = zr * zr - zi * zi + cr; zi = 2.0 * zr * zi + ci; zr = t
    return lim
sh = ".,:-=+*#%"; ins = 0
for r in range(16):
    row = ""
    for c in range(40):
        n = steps(-2.0 + c * 0.0625, -1.125 + r * 0.15, 30)
        if n == 30: row += "@"; ins += 1
        else: row += sh[n * len(sh) // 30]
    print(row)
print(f"{ins} of 640 points stayed bounded")
