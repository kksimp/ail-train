L = 200
p = [True] * (L + 1); p[0] = p[1] = False
for i in range(2, int(L ** 0.5) + 1):
    if p[i]:
        for m in range(i * i, L + 1, i): p[m] = False
w = lambda n: [a for a in range(2, n // 2 + 1) if p[a] and p[n - a]]
for n in [4, 28, 100, 128, 196]:
    ws = w(n); f = ws[0]
    print(f"{n} = {f} + {n - f} ({len(ws)} ways)")
ev = [n for n in range(4, L + 1) if n % 2 == 0]
best = ev[0]
for n in ev:
    if len(w(n)) > len(w(best)): best = n
print(f"most ways up to {L}: {best}")
