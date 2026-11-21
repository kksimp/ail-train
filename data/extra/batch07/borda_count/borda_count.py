O = ["Park", "Pool", "Library", "Gym"]; B = [(8, ["Park", "Library", "Gym", "Pool"]), (6, ["Pool", "Library", "Park", "Gym"]), (5, ["Gym", "Library", "Pool", "Park"]), (3, ["Library", "Park", "Pool", "Gym"])]
P = {o: 0 for o in O}; F = {}
for c, od in B:
    for i, o in enumerate(od): P[o] += c * (len(od) - 1 - i)
    F[od[0]] = F.get(od[0], 0) + c
for o in sorted(O, key=lambda o: (-P[o], o)): print(f"{o:<8} {P[o]:>3} points, {F.get(o, 0)} first choices")
print(f"Borda winner {max(O, key=lambda o: (P[o], o))}; most first choices {max(O, key=lambda o: (F.get(o, 0), o))}")
