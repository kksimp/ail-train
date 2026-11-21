import math
def h(ps):
    t = 0.0
    for p in ps:
        if p > 0.0:
            t -= p * math.log(p) / math.log(2.0)
    return t
def tidy(v):
    return 0.0 if abs(v) < 0.00005 else v
def report(name, counts):
    total = sum(sum(r) for r in counts)
    tf = float(total)
    rows = [sum(r) / tf for r in counts]
    cols = [sum(r[j] for r in counts) / tf for j in range(len(counts[0]))]
    joint = []
    direct = 0.0
    for i in range(len(counts)):
        for j in range(len(counts[i])):
            p = counts[i][j] / tf
            joint.append(p)
            if p > 0.0:
                direct += p * math.log(p / (rows[i] * cols[j])) / math.log(2.0)
    mi = h(rows) + h(cols) - h(joint)
    print(f"{name}: H(X) {h(rows):.4f}, H(Y) {h(cols):.4f}, H(X,Y) {h(joint):.4f}")
    print(f"    I(X;Y) = {tidy(mi):.4f} bits, summed directly {tidy(direct):.4f}")
report("rain vs umbrella", [[30, 5], [10, 55]])
report("two fair coins", [[25, 25], [25, 25]])
report("copied bit", [[50, 0], [0, 50]])
report("grade vs seat row", [[12, 6, 2], [8, 10, 7], [3, 6, 11]])
