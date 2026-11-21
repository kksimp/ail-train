def parse(dart):
    mult = {'D': 2, 'T': 3}.get(dart[0], 1)
    return (int(dart[1:]), mult)

names = ["Kim", "Lee"]
targets = [15, 16, 17, 18, 19, 20, 25]
marks = [{}, {}]
points = [0, 0]
turns = ["T20 S20 S19", "T20 T19 S5", "T19 S20 D18", "T18 S1 S20", "T17 D17 S16", "T16 D25 S25", "T15 T16 S17", "S15 D15 D25", "T20 D17 D16", "S25 D25 S25"]
for t, turn in enumerate(turns):
    p = t % 2
    o = 1 - p
    for dart in turn.split(" "):
        n, mult = parse(dart)
        if n not in targets:
            continue
        have = marks[p].get(n, 0)
        closing = min(max(3 - have, 0), mult)
        extra = mult - closing
        marks[p][n] = have + closing
        if extra > 0 and marks[o].get(n, 0) < 3:
            points[p] += extra * n
    closed = sum(1 for x in targets if marks[p].get(x, 0) == 3)
    print(f"{names[p]} throws {turn}: {closed} closed, {points[p]} points")
    if closed == 7 and points[p] >= points[o]:
        print(f"{names[p]} wins")
        break
