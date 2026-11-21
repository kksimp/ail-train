def grow(template, rules, steps):
    pairs = {}
    for i in range(1, len(template)):
        k = template[i - 1] + template[i]; pairs[k] = pairs.get(k, 0) + 1
    for _ in range(steps):
        nxt = {}
        for p, n in pairs.items():
            if p in rules:
                m = rules[p]
                for k in (p[0] + m, m + p[1]):
                    nxt[k] = nxt.get(k, 0) + n
            else:
                nxt[p] = nxt.get(p, 0) + n
        pairs = nxt
    counts = {}
    for p, n in pairs.items():
        counts[p[0]] = counts.get(p[0], 0) + n
    counts[template[-1]] = counts.get(template[-1], 0) + 1
    return max(counts.values()) - min(counts.values())

template = "DABC"
lines = ["AA -> B", "AB -> C", "AC -> A", "AD -> D", "BA -> D", "BB -> A", "BC -> B", "BD -> C", "CA -> C", "CB -> D", "CC -> B", "CD -> A", "DA -> B", "DB -> B", "DC -> C", "DD -> A"]
rules = dict(l.split(" -> ") for l in lines)
print(f"template {template}, {len(rules)} rules")
for s in [1, 2, 5]:
    print(f"after {s} steps: spread {grow(template, rules, s)}")
print(f"part 1: after 10 steps: {grow(template, rules, 10)}")
print(f"part 2: after 30 steps: {grow(template, rules, 30)}")
