groups = [(12, ["Ash", "Bea"]), (9, ["Bea", "Ash", "Cy"]), (5, ["Cy", "Bea"]), (4, ["Dee", "Cy"]), (6, ["Eve", "Dee", "Cy"]), (3, ["Bea", "Eve"]), (1, ["Cy"])]

def top(p, out):
    for c in p[0]:
        if c not in out:
            return c
    return ""

def milli(v):
    return f"{v // 1000}.{str(v % 1000).rjust(3, '0')}"

papers = []
for count, prefs in groups:
    for k in range(count):
        papers.append([prefs, 1000])
cands = ["Ash", "Bea", "Cy", "Dee", "Eve"]
seats = 2
quota = (len(papers) // (seats + 1) + 1) * 1000
print(f"{len(papers)} papers, quota {milli(quota)}")
out = set()
elected = []
rnd = 1
while len(elected) < seats:
    tallies = {}
    for c in cands:
        if c not in out:
            tallies[c] = 0
    for p in papers:
        t = top(p, out)
        if t != "":
            tallies[t] += p[1]
    shown = ", ".join(f"{k} {milli(tallies[k])}" for k in tallies)
    print(f"round {rnd}: {shown}")
    best = sorted(tallies.keys(), key=lambda k: -tallies[k])[0]
    if tallies[best] >= quota or len(tallies) <= seats - len(elected):
        elected.append(best)
        surplus = tallies[best] - quota
        for p in papers:
            if top(p, out) == best:
                p[1] = p[1] * max(surplus, 0) // tallies[best]
        out.add(best)
        print(f"  {best} elected, surplus {milli(max(surplus, 0))}")
    else:
        low = sorted(tallies.keys(), key=lambda k: tallies[k])[0]
        out.add(low)
        print(f"  {low} eliminated")
    rnd += 1
print(f"elected: {' and '.join(elected)}")
