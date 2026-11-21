def uncovered_gain(site, covered):
    return sum(1 for v in site if v not in covered)

sites = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [1, 8], [2, 3, 9, 10], [4, 5, 6, 7, 11, 12, 13, 14], [1, 2, 8]]
universe = 14
covered = set()
chosen = []
while len(covered) < universe:
    best = -1
    gain = 0
    for i in range(len(sites)):
        g = uncovered_gain(sites[i], covered)
        if g > gain:
            gain = g
            best = i
    chosen.append(best)
    for v in sites[best]:
        covered.add(v)
    print(f"pick site {best}: covers {gain} new villages, {len(covered)} of {universe} covered")
fewest = len(sites)
for mask in range(1, 1 << len(sites)):
    seen = set()
    used = 0
    for i in range(len(sites)):
        if ((mask >> i) & 1) == 1:
            used += 1
            for v in sites[i]:
                seen.add(v)
    if len(seen) == universe and used < fewest:
        fewest = used
print(f"greedy used {len(chosen)} sites; the best possible is {fewest}")
