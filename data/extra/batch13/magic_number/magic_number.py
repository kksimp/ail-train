def magic(leader, chaser):
    return 163 - leader[1] - chaser[2]

leader = ("Rivermen", 92, 58)
chasers = [("Bisons", 86, 64), ("Gulls", 84, 67), ("Miners", 75, 76), ("Comets", 70, 80)]
left = 162 - leader[1] - leader[2]
print(f"{leader[0]} are {leader[1]}-{leader[2]} with {left} games left")
for c in chasers:
    m = magic(leader, c)
    best_case = c[1] + (162 - c[1] - c[2])
    status = "eliminated" if m <= 0 else ("eliminated" if best_case < leader[1] + 1 else f"magic number {m}")
    print(f"{c[0]:<7} {c[1]}-{c[2]}: {status}")
overall = 0
for c in chasers:
    overall = max(overall, magic(leader, c))
print(f"clinch the division with a magic number of {overall}")
