def col(width, gutter):
    return (width - 11.0 * gutter) / 12.0

def span(width, gutter, n):
    return float(n) * col(width, gutter) + float(n - 1) * gutter

grids = [(1200.0, 24.0), (960.0, 20.0), (390.0, 12.0)]
for w, gt in grids:
    spans = " ".join(f"{n}:{span(w, gt, n):.1f}" for n in [1, 2, 3, 4, 6, 8, 12])
    print(f"{w:.0f}/{gt:.0f}: col {col(w, gt):.2f}  {spans}")
w, gt = grids[0]
x = 0.0
parts = []
for n in [3, 6, 3]:
    parts.append(f"{n} cols at x={x:.0f} w={span(w, gt, n):.0f}")
    x += span(w, gt, n) + gt
print(", ".join(parts))
print(f"row ends at {x - gt:.0f} of {w:.0f}")
