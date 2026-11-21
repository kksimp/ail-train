from itertools import permutations
from math import factorial
def count_auto(n, edges):
    adj = set()
    for a, b in edges:
        adj.add(a * 10 + b)
        adj.add(b * 10 + a)
    return sum(1 for p in permutations(range(n)) if all(p[a] * 10 + p[b] in adj for a, b in edges))

cases = [("path of 4", 4, [[0, 1], [1, 2], [2, 3]]), ("star of 4", 4, [[0, 1], [0, 2], [0, 3]]), ("K4", 4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]), ("pentagon", 5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]), ("house", 5, [[0, 1], [1, 2], [2, 3], [3, 0], [2, 4], [3, 4]]), ("prism", 6, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [0, 3], [1, 4], [2, 5]]), ("hexagon", 6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]])]
for name, n, edges in cases:
    a = count_auto(n, edges)
    print(f"{name:<10} {a:>3} symmetries of {factorial(n)} relabellings")
