def leap(y): return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
for t in ["2024-03-01", "2023-03-01", "2024-02-30", "2024-13-02", "24-01-05", "2000-12-31", "2026-11-21"]:
    p = t.split("-")
    if len(p) != 3 or len(p[0]) != 4: print(f"{t}: '{t}' is not YYYY-MM-DD"); continue
    y, m, d = map(int, p)
    if m < 1 or m > 12: print(f"{t}: month {m} does not exist"); continue
    L = [31, 29 if leap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if d < 1 or d > L[m - 1]: print(f"{t}: day {d} is past the {L[m - 1]}th"); continue
    print(f"{t}: day {sum(L[:m - 1]) + d}")
