def leader_of(h, a):
    return "H" if h > a else ("A" if a > h else "-")

def team(c):
    return "Hawks" if c == "H" else "Owls"

log = [(1, 'H', 2), (2, 'A', 3), (3, 'A', 2), (4, 'H', 3), (5, 'H', 2), (6, 'A', 2), (7, 'H', 1), (8, 'A', 3), (9, 'A', 2), (10, 'A', 2), (11, 'H', 3), (12, 'H', 3), (13, 'H', 2), (14, 'A', 1), (15, 'H', 2), (16, 'A', 3)]
home = away = 0
leader = "-"
changes = ties = big_h = big_a = 0
run_side = "-"
run = best_run = 0
best_side = "-"
for minute, side, pts in log:
    if side == "H":
        home += pts
    else:
        away += pts
    now = leader_of(home, away)
    if now == "-":
        ties += 1
    elif leader != "-" and now != leader:
        changes += 1
        print(f"min {minute:>2}: {team(now)} take the lead, {home}-{away}")
    if now != "-":
        leader = now
    big_h = max(big_h, home - away)
    big_a = max(big_a, away - home)
    if side == run_side:
        run += pts
    else:
        run_side = side
        run = pts
    if run > best_run:
        best_run = run
        best_side = side
print(f"final {home}-{away}, {changes} lead changes, tied {ties} times")
print(f"biggest leads: Hawks {big_h}, Owls {big_a}")
print(f"best run: {best_run} unanswered points by the {team(best_side)}")
