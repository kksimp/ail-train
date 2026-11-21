W = "it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness".split(" "); h = {}
for w in W: h[len(w)] = h.get(len(w), 0) + 1
for n in sorted(h): print(f"{n:>2} {'*' * h[n]}")
t = max(len(w) for w in W); print(f"mean {sum(len(w) for w in W) / len(W):.2f}, longest ({t}): {', '.join(w for w in W if len(w) == t)}")
