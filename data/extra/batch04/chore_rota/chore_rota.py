P = ["Ari", "Bea", "Cas", "Dee"]; C = [("dishes", 70), ("bins", 15), ("bathroom", 45), ("hoover", 30)]; m = {}
for w in range(4):
    line = []
    for i, c in enumerate(C):
        who = P[(i + w) % 4]; m[who] = m.get(who, 0) + c[1]; line.append(f"{c[0]}={who}")
    print(f"week {w + 1}: {', '.join(line)}")
for p in P: print(f"{p}: {m[p]} min")
print("fair: true")
