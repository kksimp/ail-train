def field(name):
    return {"l": 0, "w": 1, "h": 2}.get(name, 3)

def route(flows, part):
    at = "in"
    while at not in ("A", "R"):
        for rule in flows[at]:
            if ":" not in rule:
                at = rule; break
            cond, dest = rule.split(":")
            v = part[field(cond[0])]; n = int(cond[2:])
            if ("<" in cond and v < n) or (">" in cond and v > n):
                at = dest; break
    return at == "A"

def count(flows, at, lo, hi):
    if at == "R": return 0
    if at == "A":
        p = 1
        for i in range(4): p *= hi[i] - lo[i] + 1
        return p
    total = 0; a = list(lo); b = list(hi)
    for rule in flows[at]:
        if ":" not in rule:
            return total + count(flows, rule, a, b)
        cond, dest = rule.split(":")
        f = field(cond[0]); n = int(cond[2:])
        ya = list(a); yb = list(b)
        if "<" in cond:
            yb[f] = min(yb[f], n - 1); a[f] = max(a[f], n)
        else:
            ya[f] = max(ya[f], n + 1); b[f] = min(b[f], n)
        if ya[f] <= yb[f]:
            total += count(flows, dest, ya, yb)
        if a[f] > b[f]:
            return total
    return total

lines = ["in l<1500:low g>2600:A mid", "low w>3000:R h<800:A A", "mid h>2000:top R", "top l>2500:A w<1000:R A"]
flows = {}
for l in lines:
    w = l.split(" "); flows[w[0]] = w[1:]
parts = [[1200, 3500, 700, 100], [2000, 900, 2500, 300], [3000, 500, 2100, 2700], [1800, 1800, 1500, 1500], [2600, 1200, 3900, 400]]
s = 0
for p in parts:
    ok = route(flows, p)
    print(f"part {p}: {1 if ok else 0} way(s) to A")
    if ok: s += sum(p)
print(f"part 1: accepted ratings sum to {s}")
print(f"part 2: {count(flows, 'in', [1, 1, 1, 1], [4000, 4000, 4000, 4000])} accepted combinations")
