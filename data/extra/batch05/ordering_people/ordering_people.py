P = [("Ana", "Silva", 41), ("Ben", "Okoro", 29), ("Ana", "Silva", 23), ("Cy", "Adams", 35), ("Bea", "Okoro", 52)]
S = sorted(P, key=lambda p: (p[1], p[0], p[2]))
for f, l, a in S: print(f"{l}, {f} ({a})")
print(f"first: {S[0][0]} {S[0][1]}; last: {S[-1][0]} {S[-1][1]} {S[-1][2]}")
