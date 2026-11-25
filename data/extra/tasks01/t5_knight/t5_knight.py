import re
import sys
from collections import deque


def to_int(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else -1


def knight_dist(n, sr, sc, tr, tc):
    moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    dist = {(sr, sc): 0}
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))
    return dist.get((tr, tc), -1)


lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
n = to_int(lines[0]) if lines else 0
if n < 1:
    print("bad board")
else:
    for l in lines[1:]:
        w = l.split()
        if len(w) != 4:
            print("bad")
            continue
        v = [to_int(s) for s in w]
        if min(v) < 0 or max(v) >= n:
            print("bad")
        else:
            print(knight_dist(n, *v))
