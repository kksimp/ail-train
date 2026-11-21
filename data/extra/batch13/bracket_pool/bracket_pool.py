def score(picks, actual):
    total = 0
    worth = 1
    for r in range(len(actual)):
        for team in picks[r]:
            if team in actual[r]:
                total += worth
        worth *= 2
    return total

actual = [["Ajax", "Celta", "Fiorentina", "Genk"], ["Celta", "Genk"], ["Genk"]]
entrants = ["Mo", "Ines", "Tariq", "Vera"]
picks = [[["Ajax", "Celta", "Elche", "Genk"], ["Ajax", "Genk"], ["Genk"]], [["Ajax", "Dynamo", "Fiorentina", "Hertha"], ["Ajax", "Fiorentina"], ["Ajax"]], [["Benfica", "Celta", "Fiorentina", "Genk"], ["Celta", "Genk"], ["Celta"]], [["Ajax", "Celta", "Fiorentina", "Hertha"], ["Celta", "Hertha"], ["Hertha"]]]
table = [(name, score(picks[i], actual)) for i, name in enumerate(entrants)]
ranked = sorted(table, key=lambda t: -t[1])
for name, pts in ranked:
    print(f"{name:<6} {pts:>2}")
best = ranked[0]
champ = actual[2][0]
print(f"pool winner {best[0]} with {best[1]} of 12; champion {champ}")
