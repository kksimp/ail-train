cand = {"Ito", "Mbeki", "Novak", "Ruiz"}
ballots = ["Ito,Novak", "Ruiz", "Novak,Ruiz,Ito", "Mbeki,Novak", "Smith,Ito", "", "Ruiz,Novak"]
ap = {c: 0 for c in cand}; sp = 0
for b in ballots:
    ns = [n for n in b.split(",") if n]
    if any(n not in cand for n in ns):
        sp += 1; continue
    for n in ns: ap[n] += 1
for i, c in enumerate(sorted(ap, key=lambda c: (-ap[c], c))):
    print(f"{i + 1}. {c:<6} {ap[c]}")
print(f"spoiled: {sp}, counted: {len(ballots) - sp}")
