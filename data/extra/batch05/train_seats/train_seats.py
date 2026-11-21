St = ["York", "Leeds", "Wakefield", "Sheffield", "Derby"]; T = [[False] * 4 for _ in range(4)]
for w, a, b in [("Ana", 0, 4), ("Ben", 0, 2), ("Cat", 1, 3), ("Dan", 2, 4), ("Eli", 0, 1), ("Fin", 1, 4), ("Gil", 3, 4), ("Hao", 0, 3)]:
    g = next((s for s in range(4) if not any(T[s][x] for x in range(a, b))), -1)
    if g < 0: print(f"{w} {St[a]}-{St[b]}: no seat")
    else:
        for x in range(a, b): T[g][x] = True
        print(f"{w} {St[a]}-{St[b]}: seat {g + 1}")
for s in range(4): print(f"seat {s + 1}: " + "".join("#" if t else "-" for t in T[s]))
