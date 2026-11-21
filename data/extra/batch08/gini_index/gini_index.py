def gini(xs):
    n = len(xs); m = sum(xs) / n; return sum(abs(a - b) for a in xs for b in xs) / (2.0 * n * n * m)
for n, inc in [("Equalton", [30.0, 30.0, 30.0, 30.0, 30.0]), ("Midvale", [18.0, 25.0, 30.0, 38.0, 52.0]), ("Topford", [12.0, 15.0, 18.0, 22.0, 180.0]), ("Splitby", [10.0, 10.0, 10.0, 90.0, 90.0])]:
    print(f"{n:<9} Gini {gini(inc):.3f}, top earner holds {max(inc) / sum(inc) * 100.0:.1f}%")
