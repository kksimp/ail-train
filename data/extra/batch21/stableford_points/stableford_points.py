par = [4, 3, 5, 4, 4, 3, 4, 5, 4]
index = [3, 9, 1, 5, 2, 8, 4, 6, 7]
players = [("Ali", 6, [5, 3, 6, 5, 4, 4, 5, 6, 5]), ("Bo", 14, [6, 4, 7, 5, 6, 4, 5, 7, 6]), ("Cy", 0, [4, 3, 4, 4, 5, 3, 4, 5, 4]), ("Dee", 22, [7, 5, 8, 6, 7, 5, 6, 8, 9])]

def strokes(hcp, idx):
    return hcp // 9 + (1 if idx <= hcp % 9 else 0)

table = []
for name, hcp, cards in players:
    pts = [max(2 + par[h] - (cards[h] - strokes(hcp, index[h])), 0) for h in range(9)]
    total = sum(pts)
    gross = sum(cards)
    blobs = pts.count(0)
    table.append((name, total, gross))
    print(f"{name:<4} hcp {hcp:>2}: gross {gross}, points [{', '.join(str(x) for x in pts)}] = {total}, {blobs} blank holes")
ranked = sorted(table, key=lambda t: (-t[1], t[2]))
print(f"winner: {ranked[0][0]} with {ranked[0][1]} points")
