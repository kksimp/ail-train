def transpose_rotations(pcs):
    s = sorted(pcs)
    n = len(s)
    out = []
    for k in range(n):
        out.append([(s[(k + j) % n] - s[k] + 12) % 12 for j in range(n)])
    return out

def prime(pcs):
    inverted = [(12 - p) % 12 for p in pcs]
    cands = transpose_rotations(pcs)
    cands.extend(transpose_rotations(inverted))
    best = cands[0]
    for c in cands:
        if c[::-1] < best[::-1]:
            best = c
    return best

sets = [("C major", [0, 4, 7]), ("C minor", [0, 3, 7]), ("G7", [7, 11, 2, 5]), ("chromatic", [3, 4, 5]), ("whole tone", [0, 2, 4, 6, 8, 10]), ("Viennese", [0, 1, 6]), ("all-interval", [4, 5, 8, 10]), ("pentatonic", [1, 3, 6, 8, 10]), ("B half dim", [11, 2, 5, 9])]
seen = {}
for name, pcs in sets:
    p = prime(pcs)
    key = ",".join(str(x) for x in p)
    shared = seen.get(key, "")
    note = "" if shared == "" else f", same class as {shared}"
    if shared == "":
        seen[key] = name
    shown = "[" + ", ".join(str(x) for x in pcs) + "]"
    print(f"{name:<12} {shown} -> ({key}){note}")
