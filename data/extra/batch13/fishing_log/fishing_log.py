def verdict(rules, kept, species, cm):
    if species not in rules:
        return None, f"no rule for {species}"
    rule = rules[species]
    if cm < rule[0]:
        return None, f"under {rule[0]} cm"
    if kept.get(species, 0) >= rule[1]:
        return None, f"bag limit of {rule[1]} reached"
    return rule[1], None

rules = {"trout": [30, 2], "perch": [20, 5], "pike": [60, 1]}
catches = [("trout", 34), ("perch", 18), ("pike", 72), ("trout", 28), ("perch", 23), ("trout", 41), ("trout", 36), ("carp", 55), ("pike", 65), ("perch", 21)]
kept = {}
released = 0
for species, cm in catches:
    v, why = verdict(rules, kept, species, cm)
    if why is None:
        kept[species] = kept.get(species, 0) + 1
        print(f"{species:<6} {cm:>3} cm: keep, {kept[species]} of {v}")
    else:
        released += 1
        print(f"{species:<6} {cm:>3} cm: release, {why}")
bag = [f"{n} {s}" for s, n in kept.items()]
summary = ", ".join(bag)
print(f"kept {summary}; released {released}")
