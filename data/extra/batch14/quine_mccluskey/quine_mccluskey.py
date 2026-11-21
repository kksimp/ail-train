def merge(a, b):
    diff = 0
    out = []
    for x, y in zip(a, b):
        if x == y:
            out.append(x)
        else:
            diff += 1
            out.append("-")
    return "".join(out) if diff == 1 else ""
def covers(p, m):
    for i in range(4):
        bit = (m >> (3 - i)) & 1
        if p[i] != "-" and (p[i] == "1") != (bit == 1):
            return False
    return True
def term(p):
    vs = ["A", "B", "C", "D"]
    out = []
    for i in range(4):
        if p[i] == "1":
            out.append(vs[i])
        elif p[i] == "0":
            out.append(vs[i] + "'")
    return "".join(out)
minterms = [0, 1, 2, 5, 6, 7, 8, 9, 10, 14]
current = ["".join(str(b) for b in [(m >> 3) & 1, (m >> 2) & 1, (m >> 1) & 1, m & 1]) for m in minterms]
primes = []
while current:
    nxt = []
    used = set()
    for i in range(len(current)):
        for j in range(i + 1, len(current)):
            m = merge(current[i], current[j])
            if m != "":
                used.add(current[i])
                used.add(current[j])
                if m not in nxt:
                    nxt.append(m)
    for c in current:
        if c not in used and c not in primes:
            primes.append(c)
    current = nxt
print("prime implicants: " + ", ".join(term(p) for p in primes))
chosen = []
for m in minterms:
    cov = [p for p in primes if covers(p, m)]
    if len(cov) == 1 and cov[0] not in chosen:
        chosen.append(cov[0])
print("essential: " + ", ".join(term(p) for p in chosen))
left = [m for m in minterms if not any(covers(p, m) for p in chosen)]
while left:
    best = sorted(primes, key=lambda p: -len([m for m in left if covers(p, m)]))[0]
    chosen.append(best)
    left = [m for m in left if not covers(best, m)]
print("minimal sum: " + " + ".join(term(p) for p in chosen))
