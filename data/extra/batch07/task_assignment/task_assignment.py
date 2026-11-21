from itertools import permutations
W = ["Ann", "Bo", "Cal", "Dee"]; J = ["wiring", "plumbing", "painting", "tiling"]; C = [[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]
def pe(n):
    if n == 0: return [[]]
    o = []
    for p in pe(n - 1):
        for pos in range(len(p) + 1): q = p[:]; q.insert(pos, n - 1); o.append(q)
    return o
b = 1000; bp = []
for p in pe(4):
    t = sum(C[w][p[w]] for w in range(4))
    if t < b: b = t; bp = p
for w in range(4): print(f"{W[w]} -> {J[bp[w]]} ({C[w][bp[w]]} h)")
print(f"best total {b} h"); tk = set(); g = 0
for w in range(4):
    pk = -1
    for j in range(4):
        if j not in tk and (pk < 0 or C[w][j] < C[w][pk]): pk = j
    tk.add(pk); g += C[w][pk]
print(f"greedy total {g} h")
