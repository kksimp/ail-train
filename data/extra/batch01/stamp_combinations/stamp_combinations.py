def ways(vals, t):
    tb = [0] * (t + 1); tb[0] = 1
    for v in vals:
        for a in range(v, t + 1):
            tb[a] += tb[a - v]
    return tb[t]
def fewest(vals, t):
    big = t + 1
    b = [big] * (t + 1); b[0] = 0
    for a in range(1, t + 1):
        for v in vals:
            if v <= a and b[a - v] + 1 < b[a]:
                b[a] = b[a - v] + 1
    return None if b[t] == big else b[t]
stamps = [1, 5, 12, 25]
for p in [0, 7, 16, 29, 50, 63]:
    n = fewest(stamps, p)
    print(f"{p:>3}c: {ways(stamps, p):>4} ways, fewest {n if n is not None else '-'}")
print("with 5c and 12c, cannot make: " + " ".join(str(p) for p in range(1, 30) if fewest([5, 12], p) is None))
