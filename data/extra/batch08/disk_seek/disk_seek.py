def travel(s, order):
    pos = s; m = 0
    for c in order: m += abs(c - pos); pos = c
    return m
def sf(s, reqs):
    left = list(reqs); pos = s; order = []
    while left:
        pick = 0
        for i in range(len(left)):
            g = abs(left[i] - pos); b = abs(left[pick] - pos)
            if g < b or (g == b and left[i] < left[pick]): pick = i
        pos = left[pick]; order.append(pos); left.pop(pick)
    return order
head = 53; reqs = [98, 183, 37, 122, 14, 124, 65, 67]; sr = sorted(reqs)
sweep = [c for c in sr if c <= head][::-1] + [0] + [c for c in sr if c > head]
look = [c for c in sr if c <= head][::-1] + [c for c in sr if c > head]
for n, o in [("first come", reqs), ("shortest seek", sf(head, reqs)), ("sweep", sweep), ("look", look)]:
    print(f"{n:<13} {travel(head, o):>4} cylinders: {' '.join(str(c) for c in o)}")
