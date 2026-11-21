Q = [("Capital of Peru?", ["Lima", "Quito", "Bogota", "La Paz"], 0), ("Largest planet?", ["Mars", "Jupiter", "Venus", "Saturn"], 1), ("2 to the 10th?", ["1000", "1024", "512", "2048"], 1), ("Fastest land animal?", ["Lion", "Horse", "Cheetah", "Hare"], 2)]
L = "ABCD"; key = []
for qi, (t, o, r) in enumerate(Q):
    k = (qi * 3 + 1) % 4; sh = [o[(i + k) % 4] for i in range(4)]; nr = (r - k + 4) % 4
    print(f"{qi + 1}. {t}")
    for i, x in enumerate(sh): print(f"   {L[i]}) {x}")
    key.append(f"{qi + 1}{L[nr]}")
print(f"key: {' '.join(key)}")
