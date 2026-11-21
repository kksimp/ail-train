def rt(g): n = len(g); return [[g[n - 1 - c][r] for c in range(n)] for r in range(n)]
s = [list(x) for x in ["abc", "def", "ghi"]]; g = s
for t in range(1, 5):
    g = rt(g)
    if t < 4:
        print(f"after {t * 90}:")
        for r in g: print("".join(r))
print(f"back to start: {'true' if g == s else 'false'}")
