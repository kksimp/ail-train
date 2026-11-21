def before(rules, a, b):
    return f"{a}|{b}" in rules

def valid(rules, pages):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if before(rules, pages[j], pages[i]):
                return False
    return True

def reorder(rules, pages):
    out = []
    for p in pages:
        at = len(out)
        for i, q in enumerate(out):
            if before(rules, p, q):
                at = i; break
        out.insert(at, p)
    return out

rules = {"11|23", "11|35", "23|35", "47|11", "47|23", "35|52", "23|52", "11|52", "47|35", "47|52"}
updates = [[47, 11, 23, 35, 52], [11, 47, 35], [23, 52, 35], [47, 23, 52], [52, 11, 47, 23, 35]]
p1 = p2 = 0
for u in updates:
    if valid(rules, u):
        print(f"{u} is in order, middle {u[len(u) // 2]}")
        p1 += u[len(u) // 2]
    else:
        fixed = reorder(rules, u)
        print(f"{u} becomes {fixed}, middle {fixed[len(fixed) // 2]}")
        p2 += fixed[len(fixed) // 2]
print(f"part 1: {p1}")
print(f"part 2: {p2}")
