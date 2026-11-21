shelf = [("book", "Piranesi", 544), ("film", "Arrival", 116), ("book", "Tech Essays", 134), ("film", "Heat", 170), ("book", "Novella", 120), ("film", "Paprika", 80)]
o = sorted(shelf, key=lambda m: m[2])
for k, t, m in o: print(f"{k} '{t}' ({m} min)")
used = 0; picks = []
for k, t, m in o:
    if used + m <= 300: used += m; picks.append(t)
print(f"flight of 300 min: {', '.join(picks)} ({used} min)")
a = sum(m[2] for m in shelf)
print(f"whole library: {a // 60} h {a % 60} min")
