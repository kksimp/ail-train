def expected(scored, allowed):
    s = float(scored * scored)
    a = float(allowed * allowed)
    return s / (s + a)

teams = [("Foxes", 812, 690, 90, 72), ("Owls", 701, 705, 86, 76), ("Rams", 650, 742, 78, 84), ("Jays", 755, 640, 85, 77), ("Bulls", 610, 801, 62, 100)]
print("team    RS   RA   W  exp   luck")
luckiest = ""
most = -100.0
for name, rs, ra, won, lost in teams:
    games = won + lost
    exp_wins = expected(rs, ra) * float(games)
    luck = float(won) - exp_wins
    print(f"{name:<6} {rs:>4} {ra:>4} {won:>3} {exp_wins:>5.1f} {luck:>5.1f}")
    if luck > most:
        most = luck
        luckiest = name
print(f"luckiest: {luckiest}, {most:.1f} wins above expectation")
