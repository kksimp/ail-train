class Link:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

def best_matching(links, i, used):
    if i == len(links):
        return 0
    best = best_matching(links, i + 1, used)
    l = links[i]
    if not used[l.a] and not used[l.b]:
        used[l.a] = True
        used[l.b] = True
        with_it = l.w + best_matching(links, i + 1, used)
        used[l.a] = False
        used[l.b] = False
        best = max(best, with_it)
    return best

names = ["Ada", "Ben", "Cas", "Dot", "Eli", "Fay", "Gus", "Hal"]
links = [Link(0, 1, 9), Link(1, 2, 10), Link(2, 3, 9), Link(0, 4, 4), Link(4, 5, 7), Link(5, 6, 8), Link(6, 7, 5), Link(3, 7, 6), Link(1, 5, 3), Link(2, 6, 2)]
order = sorted(links, key=lambda l: -l.w)
taken = [False] * 8
total = 0
for l in order:
    if not taken[l.a] and not taken[l.b]:
        taken[l.a] = True
        taken[l.b] = True
        total += l.w
        print(f"pair {names[l.a]} + {names[l.b]} ({l.w})")
used = [False] * 8
best = best_matching(links, 0, used)
print(f"greedy total {total}, best possible {best}")
