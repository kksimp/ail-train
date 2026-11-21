P = {"G": 3, "P": 1, "L": 2}
logs = [("no.4", "GPP"), ("no.7", "L"), ("no.9", "GLPP"), ("no.12", ""), ("no.15", "PLLGG")]
bd = []
for h, b in logs:
    base = sum(P[x] for x in b); bo = 5 if all(x in b for x in "GPL") else 0
    bd.append((h, base + bo)); print(f"{h:<6} {len(b)} bags, {base} points + {bo} bonus")
w = max(bd, key=lambda x: x[1]); print(f"top: {w[0]} with {w[1]}")
