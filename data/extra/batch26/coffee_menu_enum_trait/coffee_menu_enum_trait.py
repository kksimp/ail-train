def price(d):
    k = d[0]
    if k == "E": return 220
    if k == "L": return 360 if d[1] else 330
    if k == "M": return 350 + (d[1] - 1) * 60
    return 250
def label(d):
    k = d[0]
    if k == "E": return "espresso"
    if k == "L": return "oat latte" if d[1] else "latte"
    if k == "M": return f"mocha x{d[1]}"
    return f"tea ({d[1]} min)"
m = lambda c: f"{c // 100}.{c % 100:02}"
tables = [[("E",), ("L", True), ("M", 2)], [("T", 4), ("L", False), ("L", False)], [("M", 3), ("E",)]]
for i, t in enumerate(tables):
    print(f"table {i + 1}: {', '.join(label(d) for d in t)} = {m(sum(price(d) for d in t))}")
allx = [d for t in tables for d in t]
best = allx[0]
for d in allx:
    if price(d) > price(best): best = d
print(f"dearest drink: {label(best)} at {m(price(best))}")
