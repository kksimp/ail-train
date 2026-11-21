def try_set(lit, imp, val):
    v = list(val)
    queue = [lit]
    while queue:
        q = queue.pop()
        want = 1 - q % 2
        if v[q // 2] == want:
            continue
        if v[q // 2] != -1:
            return []
        v[q // 2] = want
        for nxt in imp.get(q, []):
            queue.append(nxt)
    return v

def solve(n, rules):
    imp = {}
    for r in rules:
        a = 2 * r[0] + 1 - r[1]
        b = 2 * r[2] + 1 - r[3]
        imp.setdefault(a ^ 1, []).append(b)
        imp.setdefault(b ^ 1, []).append(a)
    val = [-1 for t in range(n)]
    for x in range(n):
        if val[x] == -1:
            first = try_set(2 * x, imp, val)
            second = first if len(first) > 0 else try_set(2 * x + 1, imp, val)
            if len(second) == 0:
                return second
            val = second
    return val

teams = ["Ann", "Bob", "Cy", "Di"]
base = [[0, 1, 1, 1], [0, 0, 1, 0], [1, 1, 2, 0], [2, 1, 3, 1], [3, 0, 0, 0], [2, 0, 3, 0]]
tight = list(base)
for r in [[0, 1, 2, 1], [0, 1, 2, 0], [0, 0, 3, 1], [0, 0, 3, 0]]:
    tight.append(r)
for rules in [base[0:3], base, tight]:
    val = solve(len(teams), rules)
    plan = []
    for t in range(len(val)):
        slot = "AM" if val[t] == 1 else "PM"
        plan.append(f"{teams[t]} {slot}")
    shown = "no plan meets every rule" if len(plan) == 0 else ", ".join(plan)
    print(f"{len(rules)} rules: {shown}")
