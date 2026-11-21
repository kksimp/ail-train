T = {}
for e, g, s, b in [("100m", "KEN", "USA", "JAM"), ("long jump", "USA", "GER", "KEN"), ("400m", "JAM", "USA", "GBR"), ("high jump", "GER", "GBR", "USA"), ("1500m", "KEN", "KEN", "GBR"), ("relay", "USA", "JAM", "GER"), ("javelin", "GER", "FIN", "KEN")]:
    for c in (g, s, b): T.setdefault(c, [0, 0, 0])
    T[g][0] += 1; T[s][1] += 1; T[b][2] += 1
for i, c in enumerate(sorted(T, key=lambda c: (-T[c][0], -T[c][1], -T[c][2], c))): m = T[c]; print(f"{i + 1}. {c} {m[0]} {m[1]} {m[2]} (total {sum(m)})")
