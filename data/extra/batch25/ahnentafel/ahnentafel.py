def generation(n):
    g = 0
    x = n
    while x > 1:
        x = x // 2
        g += 1
    return g

def relation(n):
    steps = []
    x = n
    while x > 1:
        steps.insert(0, "father" if x % 2 == 0 else "mother")
        x = x // 2
    if not steps:
        return "self"
    last = steps.pop()
    parts = [s + "'s" for s in steps]
    parts.append(last)
    return " ".join(parts)

known = [(1, "Rosa Lind"), (2, "Peter Lind"), (3, "Ana Costa"), (4, "Hugo Lind"), (5, "Marta Berg"), (7, "Ines Duarte"), (9, "Clara Holm"), (10, "Olof Berg"), (14, "Rui Duarte"), (15, "Lucia Ramos"), (29, "Teresa Vaz")]
for n, name in known:
    child = "-" if n == 1 else str(n // 2)
    print(f"{n:>2} {name:<12} gen {generation(n)}  child {child:<2}  {relation(n)}")
found = [0, 0, 0, 0, 0]
for n, name in known:
    found[generation(n)] += 1
for g in range(1, 5):
    slots = 1 << g
    print(f"generation {g}: {found[g]} of {slots} ancestors known")
