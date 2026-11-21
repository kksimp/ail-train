def thin(ps, gap):
    kept = []
    for p in sorted(ps):
        last = kept[-1] if kept else -1000
        if p - last >= gap:
            kept.append(p)
    return kept

branches = [[5, 9, 22, 30, 31, 47, 60], [12, 14, 16, 40, 41, 55, 58, 71, 90], [3, 18, 33, 48], [70, 8, 25, 26, 52]]
kept_all = picked = 0
for i, b in enumerate(branches):
    k = thin(b, 15)
    kept_all += len(k)
    picked += len(b) - len(k)
    print(f"branch {i + 1}: keep [{', '.join(str(x) for x in k)}] ({len(b) - len(k)} picked off)")
grams = kept_all * 150
print(f"{kept_all} kept, {picked} removed; expected crop about {grams // 1000}.{grams % 1000 // 100} kg")
