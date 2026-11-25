import sys
from collections import deque


def adjacent(a, b):
    return len(a) == len(b) and sum(1 for x, y in zip(a, b) if x != y) == 1


lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
first = lines[0].split() if lines else []
if len(first) != 2:
    print("bad input")
    sys.exit(0)
start, goal = first
words = {start}
words.update(lines[1:])
if goal not in words:
    print("no ladder")
    sys.exit(0)
allw = sorted(words)
parent = {}
seen = {start}
q = deque([start])
while q and goal not in seen:
    cur = q.popleft()
    for w in allw:
        if w not in seen and adjacent(cur, w):
            seen.add(w)
            parent[w] = cur
            q.append(w)
if goal not in seen:
    print("no ladder")
    sys.exit(0)
path = [goal]
while path[-1] != start:
    path.append(parent[path[-1]])
path.reverse()
print(f"length: {len(path)}")
print("path: " + " -> ".join(path))
