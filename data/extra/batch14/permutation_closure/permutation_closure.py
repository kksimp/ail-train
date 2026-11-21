def compose(a, b):
    return [a[b[i]] for i in range(len(b))]
def is_even(p):
    seen = [False] * len(p)
    swaps = 0
    for s in range(len(p)):
        x = s
        l = 0
        while not seen[x]:
            seen[x] = True
            x = p[x]
            l += 1
        if l > 0:
            swaps += l - 1
    return swaps % 2 == 0
def generate(gens):
    ident = list(range(len(gens[0])))
    group = [ident]
    seen = {str(ident)}
    i = 0
    while i < len(group):
        for g in gens:
            c = compose(g, group[i])
            if str(c) not in seen:
                seen.add(str(c))
                group.append(c)
        i += 1
    return group
cases = [("triangle turn and flip", [[1, 2, 0], [0, 2, 1]]), ("pentagon turn and flip", [[1, 2, 3, 4, 0], [0, 4, 3, 2, 1]]), ("two 3-cycles on 4", [[1, 2, 0, 3], [0, 2, 3, 1]]), ("swap and 4-cycle", [[1, 0, 2, 3], [1, 2, 3, 0]]), ("out-shuffle of 6 cards", [[0, 2, 4, 1, 3, 5]]), ("out-shuffle and top swap", [[0, 2, 4, 1, 3, 5], [1, 0, 2, 3, 4, 5]])]
for name, gens in cases:
    g = generate(gens)
    fact = 1
    for k in range(1, len(gens[0]) + 1):
        fact *= k
    evens = len([p for p in g if is_even(p)])
    print(f"{name:<25} order {len(g):>3} of {fact:>3}, {evens} even")
