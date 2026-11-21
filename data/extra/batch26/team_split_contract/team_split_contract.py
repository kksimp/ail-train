skill = {"Ava": 9, "Ben": 4, "Cal": 7, "Dia": 8, "Eli": 3, "Fin": 6, "Gia": 5, "Hal": 2, "Ivy": 7}
order = sorted(skill, key=lambda k: (-skill[k], k))
print(f"draft order: {' '.join(order)}")
teams = [[] for _ in range(3)]
for i, n in enumerate(order): teams[i % 3].append(n)
tot = []
for i, t in enumerate(teams):
    s = sum(skill[n] for n in t); tot.append(s)
    print(f"team {i + 1}: {', '.join(t)} (skill {s})")
print(f"strongest minus weakest: {max(tot) - min(tot)}")
