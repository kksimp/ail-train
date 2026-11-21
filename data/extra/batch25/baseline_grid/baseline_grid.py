styles = [("display", 36, 120), ("heading", 24, 125), ("subhead", 20, 140), ("body", 16, 150), ("caption", 13, 160)]

def snapped(size, pct):
    return (size * pct + 799) // 800 * 8

for name, size, pct in styles:
    raw = (size * pct) / 100.0
    line = snapped(size, pct)
    print(f"{name:<8} {size}px x {pct}% = {raw:>4.1f} px -> {line} px ({line // 8} rows)")
blocks = [("display", 1), ("body", 4), ("heading", 2), ("body", 6), ("caption", 2)]
y = 0
for name, lines in blocks:
    st = [s for s in styles if s[0] == name][0]
    print(f"  {name:<8} x{lines} starts at y = {y}")
    y += snapped(st[1], st[2]) * lines
print(f"page column ends at y = {y}, on grid: {'true' if y % 8 == 0 else 'false'}")
