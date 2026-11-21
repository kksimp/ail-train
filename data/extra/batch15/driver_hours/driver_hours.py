def check(day):
    problems = []; since = 0; total = 0; had15 = False
    for kind, m in day:
        if kind == "D":
            since += m; total += m
            if since > 270:
                problems.append(f"drove {since} min without a full break"); since = 0
        elif kind == "R":
            if m >= 45 or (had15 and m >= 30):
                since = 0; had15 = False
            elif m >= 15:
                had15 = True
    if total > 540:
        problems.append(f"drove {total} min in the day (limit 540)")
    return problems
days = [[("D", 240), ("R", 45), ("D", 200), ("W", 60), ("D", 60)], [("D", 150), ("R", 15), ("D", 100), ("R", 30), ("D", 260)], [("D", 200), ("R", 20), ("D", 120), ("R", 45), ("D", 250)]]
for i, d in enumerate(days):
    problems = check(d)
    if not problems: print(f"day {i + 1}: within the rules")
    for p in problems: print(f"day {i + 1}: {p}")
