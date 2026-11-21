def vector(pcs):
    v = [0] * 6
    for i in range(len(pcs)):
        for j in range(i + 1, len(pcs)):
            d = (pcs[j] - pcs[i] + 12) % 12
            ic = min(d, 12 - d)
            if ic > 0:
                v[ic - 1] += 1
    return v

sets = [("major triad", [0, 4, 7]), ("augmented", [0, 4, 8]), ("diatonic", [0, 2, 4, 5, 7, 9, 11]), ("pentatonic", [0, 2, 4, 7, 9]), ("4-Z15", [0, 1, 4, 6]), ("4-Z29", [0, 1, 3, 7]), ("whole tone", [0, 2, 4, 6, 8, 10]), ("6-Z17", [0, 1, 2, 4, 7, 8]), ("6-Z43", [0, 1, 2, 5, 6, 8])]
by_vector = {}
for name, pcs in sets:
    v = vector(pcs)
    key = "".join(str(x) for x in v)
    by_vector.setdefault(key, []).append(name)
    distinct = len(set(v)) == 6
    tag = " (every class a different count)" if distinct else ""
    print(f"{name:<12} <{key}>{tag}")
for key, names in by_vector.items():
    if len(names) > 1:
        print(f"Z-related: {' and '.join(names)} share <{key}>")
