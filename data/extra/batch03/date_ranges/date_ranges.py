b = [(3, 7), (10, 12), (6, 9), (20, 25), (13, 14), (40, 44), (24, 30)]
for i in range(len(b)):
    for j in range(i + 1, len(b)):
        if b[i][0] <= b[j][1] and b[j][0] <= b[i][1]: print(f"overlap: {b[i]} and {b[j]}")
out = []
for r in sorted(b):
    if not out or out[-1][1] < r[0] - 1: out.append(r)
    else: out[-1] = (out[-1][0], max(out[-1][1], r[1]))
print(f"busy: {out}")
g = []; d = 1
for x in out:
    if x[0] > d: g.append((d, x[0] - 1))
    d = x[1] + 1
if d <= 60: g.append((d, 60))
print(f"free: {g}")
