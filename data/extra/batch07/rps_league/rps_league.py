def be(a, b): return (a, b) in [(0, 2), (1, 0), (2, 1)]
def pl(s, r, lo): return 0 if s == 0 else r % 3 if s == 1 else (lo + 1) % 3 if s == 2 else (r * r + 1) % 3
N = ["Rocky", "Cycler", "Copycat-beater", "Squares"]; P = [0] * 4
for a in range(4):
    for b in range(a + 1, 4):
        la = lb = wa = wb = 0
        for r in range(30):
            ma = pl(a, r, lb); mb = pl(b, r, la)
            if be(ma, mb): wa += 1
            elif be(mb, ma): wb += 1
            la = ma; lb = mb
        if wa > wb: P[a] += 3
        elif wb > wa: P[b] += 3
        else: P[a] += 1; P[b] += 1
        print(f"{N[a]} v {N[b]}: {wa}-{wb}")
for i in sorted(range(4), key=lambda i: (-P[i], i)): print(f"{N[i]:<15} {P[i]}")
