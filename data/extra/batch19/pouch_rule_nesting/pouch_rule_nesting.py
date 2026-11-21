def can_hold(rules, outer, target):
    return any(inner == target or can_hold(rules, inner, target) for inner in rules[outer])

def inside(rules, colour):
    return sum(n * (1 + inside(rules, inner)) for inner, n in rules[colour].items())

lines = ["red: 2 gold, 1 teal", "teal: 3 plum", "gold: 2 plum, 1 sand", "plum: none", "sand: 4 plum", "jade: 1 red", "rust: 2 teal, 1 sand", "lime: 5 jade"]
rules = {}
for l in lines:
    k, v = l.split(": ")
    holds = {}
    if v != "none":
        for part in v.split(", "):
            n, c = part.split(" "); holds[c] = int(n)
    rules[k] = holds
outers = [c for c in rules if can_hold(rules, c, "gold")]
print(f"colours that can hold gold: {', '.join(outers)}")
print(f"part 1: {len(outers)}")
print(f"part 2: a gold pouch holds {inside(rules, 'gold')} pouches")
