posts = [("intro", ["ail", "start"]), ("empty", []), ("tasks", ["ail", "tasks", "channels"])]
tags = [t for _, ts in posts for t in ts]
print(" ".join(tags))
print(" ".join(sorted(set(tags))))
table = [[1, 2, 3], [], [4], [5, 6]]
cells = [c for row in table for c in row]
print(",".join(map(str, cells)))
print(sum(cells))
print(",".join(str(len(r)) for r in table))
print(" ".join(str(v) for n in [1, 2, 3] for v in (n, n * n)))
print(len([w for s in ["a b", "c", "d e f"] for w in s.split(" ")]))
