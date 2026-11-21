def add_all(target, items):
    grew = False
    for x in items:
        if x not in target:
            target.append(x)
            grew = True
    return grew

prods = [["E", "T", "E'"], ["E'", "+", "T", "E'"], ["E'"], ["T", "F", "T'"], ["T'", "*", "F", "T'"], ["T'"], ["F", "(", "E", ")"], ["F", "id"]]
firsts = {}
nullable = {}
for p in prods:
    firsts[p[0]] = []
    nullable[p[0]] = False
rounds = 0
changed = True
while changed:
    changed = False
    rounds += 1
    for p in prods:
        lhs = p[0]
        cur = firsts[lhs]
        all_empty = True
        for sym in p[1:]:
            if sym in firsts:
                if add_all(cur, list(firsts[sym])):
                    changed = True
                if not nullable[sym]:
                    all_empty = False
                    break
            else:
                if add_all(cur, [sym]):
                    changed = True
                all_empty = False
                break
        firsts[lhs] = cur
        if all_empty and not nullable[lhs]:
            nullable[lhs] = True
            changed = True
for nt, fs in firsts.items():
    shown = " ".join(sorted(fs))
    tail = " (can be empty)" if nullable[nt] else ""
    print(f"FIRST({nt:<2}) = {{ {shown} }}{tail}")
print(f"settled after {rounds} passes")
