from collections import deque
room = ["#####D#####", "#.........#", "#.p.p..p..#", "#..p...p..D", "#.p..p....#", "#...p...p.#", "###########"]
g = [list(l) for l in room]
h = len(g); w = len(g[0])
dist = [[0 if g[r][c] == 'D' else -1 for c in range(w)] for r in range(h)]
q = deque(r * w + c for r in range(h) for c in range(w) if g[r][c] == 'D')
while q:
    p = q.popleft()
    for n in [p - w, p + w, p - 1, p + 1]:
        if 0 <= n < h * w and g[n // w][n % w] != '#' and dist[n // w][n % w] < 0:
            dist[n // w][n % w] = dist[p // w][p % w] + 1
            q.append(n)
people = [r * w + c for r in range(h) for c in range(w) if g[r][c] == 'p']
out_by = {}
tick = 0
D = lambda p: dist[p // w][p % w]
while people:
    tick += 1
    order = sorted(people, key=lambda p: (D(p), p))
    taken = set(people)
    used = set()
    stay = []
    for p in order:
        best = p; gone = False
        for n in [p - w, p + w, p - 1, p + 1]:
            ch = g[n // w][n % w]
            if ch == 'D' and n not in used and not gone:
                used.add(n); out_by[n] = out_by.get(n, 0) + 1; gone = True
            elif ch != '#' and ch != 'D' and n not in taken and D(n) < D(best):
                best = n
        taken.discard(p)
        if not gone:
            taken.add(best); stay.append(best)
    people = stay
    print(f"tick {tick}: {len(people)} still inside")
for door, n in out_by.items():
    print(f"door at row {door // w}, column {door % w}: {n} people")
