teams = [("Quizzly Bears", 41), ("Know-it-Owls", 47), ("Les Quizerables", 41), ("Trivia Newton", 38), ("Agatha Quiztie", 47), ("Pub Brains", 29)]
r = sorted(teams, key=lambda t: -t[1])
ps = []
for i, t in enumerate(r):
    ps.append(ps[i - 1] if i > 0 and t[1] == r[i - 1][1] else i + 1)
for i, t in enumerate(r):
    tie = "=" if i > 0 and ps[i] == ps[i - 1] else " "
    print(f"{ps[i]}{tie} {t[0]:<16} {t[1]}")
print(f"{sum(1 for p in ps if ps.count(p) > 1)} teams share a place")
