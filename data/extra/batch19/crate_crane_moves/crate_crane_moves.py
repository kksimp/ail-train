def run_crane(start, moves, grab):
    piles = [list(p) for p in start]
    for line in moves:
        w = line.split(" ")
        n = int(w[1]); a = int(w[3]) - 1; b = int(w[5]) - 1
        lift = []
        for _ in range(n):
            lift.append(piles[a].pop() if piles[a] else '?')
        if grab:
            lift.reverse()
        piles[b].extend(lift)
    return "".join(p[-1] if p else '-' for p in piles)

start = ["RTK", "MBQL", "SF", "DWNC"]
moves = ["move 2 from 2 to 1", "move 1 from 4 to 3", "move 3 from 1 to 3", "move 2 from 4 to 2", "move 1 from 3 to 4", "move 4 from 3 to 2"]
for i, p in enumerate(start):
    print(f"pile {i + 1} bottom to top: {p}")
print(f"{len(moves)} orders on the board")
print(f"part 1, one crate at a time: tops {run_crane(start, moves, False)}")
print(f"part 2, grab several at once: tops {run_crane(start, moves, True)}")
