def pr(o): return 2 if o in "*/" else 1
def rp(T):
    o = []; s = []
    for t in T:
        if t == "(": s.append(t)
        elif t == ")":
            while s[-1] != "(": o.append(s.pop())
            s.pop()
        elif t in "+-*/":
            while s and s[-1] != "(" and pr(s[-1]) >= pr(t): o.append(s.pop())
            s.append(t)
        else: o.append(t)
    while s: o.append(s.pop())
    return o
def rn(R):
    s = []
    for t in R:
        if t in "+-*/":
            b = s.pop(); a = s.pop(); s.append(a + b if t == "+" else a - b if t == "-" else a * b if t == "*" else a // b)
        else: s.append(int(t))
    return s.pop()
for e in ["3 + 4 * 2", "( 3 + 4 ) * 2", "100 / ( 2 + 3 ) - 7", "8 - 3 - 2", "2 * ( 3 + 4 ) * ( 5 - 1 )"]:
    r = rp(e.split(" ")); print(f"{e} => {' '.join(r)} = {rn(r)}")
