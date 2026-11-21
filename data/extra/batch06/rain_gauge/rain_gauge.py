G = [[0, 12, 5, -1, 0, 22, 3], [1, 10, -1, 0, 0, 25, 4], [0, -1, 6, 0, 1, 19, -1]]; D = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]; M = []
for d in range(7):
    v = [g[d] for g in G if g[d] >= 0]; m = sum(v) / len(v); M.append(m); print(f"{D[d]}: {len(v)} gauges, mean {m:.1f} mm")
w = max(range(7), key=lambda d: (M[d], -d)); print(f"wettest {D[w]}, dry: {', '.join(D[d] for d in range(7) if M[d] < 0.5)}")
