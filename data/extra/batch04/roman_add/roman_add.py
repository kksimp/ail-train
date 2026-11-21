V = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
def pa(s): return sum(-V[c] if i + 1 < len(s) and V[c] < V[s[i + 1]] else V[c] for i, c in enumerate(s))
T = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
def rd(n):
    o = ""
    for v, s in T:
        while n >= v: o += s; n -= v
    return o
for a, b in [("XIV", "XXVIII"), ("MCMXC", "XXXIV"), ("CDXLIV", "DLVI"), ("IX", "IX")]:
    t = pa(a) + pa(b); print(f"{a} + {b} = {rd(t)} ({t})")
