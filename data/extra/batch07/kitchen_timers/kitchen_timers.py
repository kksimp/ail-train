T = [("pasta", 30, 600), ("sauce", 0, 1500), ("bread", 120, 1080), ("eggs", 400, 420), ("tea", 900, 240)]
E = sorted((s + d, n) for n, s, d in T); pv = 0; g = (0, ""); c = lambda s: f"{s // 60}:{s % 60:02}"
for e in E:
    print(f"{c(e[0])} {e[1]}")
    if e[0] - pv > g[0]: g = (e[0] - pv, e[1])
    pv = e[0]
print(f"longest quiet spell: {c(g[0])} before {g[1]}")
