from collections import deque
def sq(s): return (ord(s[0]) - 97, ord(s[1]) - 49)
def mb(a, b):
    s, g = sq(a), sq(b); d = {s: 0}; q = deque([s])
    while q:
        c = q.popleft()
        if c == g: return d[c]
        for dx, dy in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            n = (c[0] + dx, c[1] + dy)
            if 0 <= n[0] < 8 and 0 <= n[1] < 8 and n not in d: d[n] = d[c] + 1; q.append(n)
    return -1
for a, b in [("a1", "b3"), ("a1", "h8"), ("d4", "d5"), ("a1", "b2"), ("g7", "g7"), ("b1", "g1")]: print(f"{a} -> {b}: {mb(a, b)}")
