S = [("Ada", 6312), ("Bo", 5987), ("Cy", 6420), ("Di", 6105), ("Ed", 5899), ("Flo", 6255), ("Gus", 6033), ("Hal", 6688), ("Ivy", 6140), ("Jo", 6501), ("Kai", 5950), ("Lu", 6377)]
La = [3, 4, 2, 5, 1, 6]; F = sorted(S, key=lambda s: (s[1], s[0])); H = (len(F) + 5) // 6
def mm(t): return f"{t // 6000}:{t // 100 % 60:02}.{t % 100:02}"
for h in range(H):
    G = F[h * 6:min((h + 1) * 6, len(F))]; print(f"heat {H - h}:")
    for l, s in sorted((La[i], f"{s[0]} {mm(s[1])}") for i, s in enumerate(G)): print(f"  lane {l}: {s}")
