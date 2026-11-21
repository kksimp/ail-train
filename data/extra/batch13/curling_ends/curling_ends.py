def score_end(stones):
    inside = sorted([s for s in stones if s[1] <= 183], key=lambda s: s[1])
    if not inside:
        return ('-', 0)
    lead = inside[0][0]
    n = 0
    for s in inside:
        if s[0] != lead:
            break
        n += 1
    return (lead, n)

ends = ["R40 Y95 R120 Y150 R200", "Y30 Y60 R70 Y110 R160", "R250 Y300", "R15 R50 R80 Y90 Y175", "Y45 R46 Y100 R130", "R20 Y25 R60 R61 Y190"]
totals = {'R': 0, 'Y': 0}
hammer = 'Y'
for i, e in enumerate(ends):
    stones = []
    for word in e.split(" "):
        stones.append((word[0], int(word[1:])))
    team, pts = score_end(stones)
    if pts == 0:
        print(f"end {i + 1}: blank, {hammer} keeps the hammer")
        continue
    totals[team] += pts
    hammer = 'Y' if team == 'R' else 'R'
    print(f"end {i + 1}: {team} scores {pts}, hammer to {hammer}; R {totals['R']} Y {totals['Y']}")
