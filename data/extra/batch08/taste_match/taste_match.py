readers = ["you", "Ana", "Bo", "Cy"]; books = ["Dune", "Emma", "Ulysses", "Beloved", "Matilda", "Kindred"]
R = [[5, 0, 1, 4, 0, 0], [5, 2, 1, 5, 4, 5], [1, 5, 4, 2, 5, 0], [4, 0, 0, 0, 2, 4]]
best = -1; bg = 100.0
for r in range(1, 4):
    sh = [b for b in range(6) if R[0][b] > 0 and R[r][b] > 0]
    if len(sh) >= 2:
        g = sum(abs(R[0][b] - R[r][b]) for b in sh) / len(sh); print(f"{readers[r]}: {len(sh)} shared, average gap {g:.2f}")
        if g < bg: best = r; bg = g
    else: print(f"{readers[r]}: only {len(sh)} shared, skipped")
picks = [books[b] for b in range(6) if R[0][b] == 0 and R[best][b] >= 4]
print(f"closest taste: {readers[best]}; try {', '.join(picks)}")
