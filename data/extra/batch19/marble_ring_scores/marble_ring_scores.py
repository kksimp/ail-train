def play(players, last):
    ring = [0]; cur = 0; scores = [0] * players
    for m in range(1, last + 1):
        if m % 13 == 0:
            n = len(ring)
            at = ((cur - 5) % n + n) % n
            scores[m % players] += m + ring[at]
            ring.pop(at)
            cur = at % len(ring)
        else:
            at = (cur + 1) % len(ring) + 1
            ring.insert(at, m); cur = at
    return max(scores)

for players in [5, 7]:
    print(f"{players} players, 40 marbles: best score {play(players, 40)}")
print(f"part 1: 9 players, 120 marbles: best score {play(9, 120)}")
print(f"part 2: 9 players, 1200 marbles: best score {play(9, 1200)}")
