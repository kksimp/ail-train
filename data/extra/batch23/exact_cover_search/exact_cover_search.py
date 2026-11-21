def search(sets, items, alive, chosen, found, nodes):
    nodes[0] += 1
    if len(items) == 0:
        found.append(" ".join(chr(65 + s) for s in chosen))
        return
    pick = -1
    fewest = 1000
    for it in items:
        c = len([s for s in range(len(sets)) if alive[s] and it in sets[s]])
        if c < fewest:
            fewest = c
            pick = it
    for s in range(len(sets)):
        if alive[s] and pick in sets[s]:
            next_alive = list(alive)
            for t in range(len(sets)):
                if next_alive[t] and any(x in sets[s] for x in sets[t]):
                    next_alive[t] = False
            rest = [x for x in items if x not in sets[s]]
            chosen.append(s)
            search(sets, rest, next_alive, chosen, found, nodes)
            chosen.pop()

def solve(title, sets, n):
    items = list(range(1, n + 1))
    alive = [True for s in sets]
    chosen = []
    found = []
    nodes = [0]
    search(sets, items, alive, chosen, found, nodes)
    shown = "none" if len(found) == 0 else " | ".join(found)
    print(f"{title}: {len(found)} exact covers ({nodes[0]} search nodes): {shown}")

knuth = [[1, 4, 7], [1, 4], [4, 5, 7], [3, 5, 6], [2, 3, 6, 7], [2, 7]]
solve("Knuth's example", knuth, 7)
teams = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7], [2, 6, 7], [4, 8, 3]]
solve("teams of three for 9 people", teams, 9)
none_case = [[1, 2], [2, 3], [1, 3]]
solve("pairs over 3 items", none_case, 3)
