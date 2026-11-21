from collections import deque
P = {(0, 0): ((0, 0), "start")}; q = [(0, 0)]; h = 0; f = None
while h < len(q):
    s = q[h]; h += 1; a, b = s
    if 4 in s: f = s; break
    ab = min(a, 5 - b); ba = min(b, 3 - a)
    for m, n in [((3, b), "fill A"), ((a, 5), "fill B"), ((0, b), "empty A"), ((a, 0), "empty B"), ((a - ab, b + ab), "pour A into B"), ((a + ba, b - ba), "pour B into A")]:
        if m not in P: P[m] = (s, n); q.append(m)
S = []; c = f
while c != (0, 0): p = P[c]; S.append(f"{p[1]} -> ({c[0]}, {c[1]})"); c = p[0]
for i, s in enumerate(reversed(S)): print(f"{i + 1}. {s}")
