steps = [("cast", 96), ("machine", 92), ("heat treat", 98), ("grind", 95), ("inspect", 97)]

def needed(out, pct):
    return (out * 100 + pct - 1) // pct

need = []
out = 1000
for i in range(len(steps)):
    k = len(steps) - 1 - i
    start = needed(out, steps[k][1])
    need.insert(0, start)
    out = start
rty = 1.0
for i, (name, pct) in enumerate(steps):
    after = need[i + 1] if i + 1 < len(steps) else 1000
    rty *= float(pct) / 100.0
    print(f"{name:<10} {pct}%: start {need[i]:>4}, pass {after:>4}, scrap {need[i] - after}")
print(f"start {need[0]} for 1000 good; rolled yield {rty * 100.0:.2f}%")
