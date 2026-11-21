def holds(kind, a, b):
    if kind == 0: return b % a == 0
    if kind == 1: return a < b
    if kind == 2: return a % 2 == b % 2
    if kind == 3: return abs(a - b) <= 1
    if kind == 4: return (a - b) % 3 == 0
    return a + b == 7
def B(v):
    return "true" if v else "false"
names = ["divides", "less than", "same parity", "within 1", "same mod 3", "sum is 7"]
xs = [1, 2, 3, 4, 5, 6]
for k in range(len(names)):
    refl = all(holds(k, a, a) for a in xs)
    sym = all(not (holds(k, a, b) and not holds(k, b, a)) for a in xs for b in xs)
    anti = all(not (holds(k, a, b) and holds(k, b, a) and a != b) for a in xs for b in xs)
    trans = all(not (holds(k, a, b) and holds(k, b, c) and not holds(k, a, c)) for a in xs for b in xs for c in xs)
    kind = "neither"
    if refl and sym and trans:
        kind = "equivalence"
    elif refl and anti and trans:
        kind = "partial order"
    elif anti and trans:
        kind = "strict order"
    print(f"{names[k]:<12} reflexive {B(refl)}, symmetric {B(sym)}, antisymmetric {B(anti)}, transitive {B(trans)}: {kind}")
    if kind == "equivalence":
        done = set()
        classes = []
        for a in xs:
            if a not in done:
                cls = [b for b in xs if holds(k, a, b)]
                done.update(cls)
                classes.append("[" + ", ".join(map(str, cls)) + "]")
        print("    classes " + " ".join(classes))
