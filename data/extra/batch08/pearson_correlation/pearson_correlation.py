def pearson(xs, ys):
    mx = sum(xs) / len(xs); my = sum(ys) / len(ys); sxy = sxx = syy = 0.0
    for i in range(len(xs)):
        dx = xs[i] - mx; dy = ys[i] - my; sxy += dx * dy; sxx += dx * dx; syy += dy * dy
    return sxy / (sxx * syy) ** 0.5
def describe(r):
    s = abs(r); st = "strong" if s >= 0.7 else "moderate" if s >= 0.4 else "weak"
    return f"{st} {'positive' if r >= 0.0 else 'negative'}"
score = [55.0, 68.0, 74.0, 48.0, 83.0, 60.0, 88.0, 70.0]
for n, xs in [("study", [2.0, 4.0, 5.0, 1.0, 6.0, 3.0, 7.0, 4.5]), ("screen", [5.0, 3.0, 2.5, 6.0, 1.0, 4.0, 2.0, 3.5]), ("shoe size", [42.0, 38.0, 44.0, 40.0, 39.0, 43.0, 41.0, 37.0])]:
    r = pearson(xs, score); print(f"{n:<9} vs score: r = {r:>6.3f} ({describe(r)})")
