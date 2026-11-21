import functools
reqs = [("Abe", False, 40, 3), ("Bea", True, 5, 2), ("Cal", False, 90, 1), ("Dot", False, 40, 1), ("Eli", True, 12, 4)]
key = lambda r: (0 if r[1] else 1, -r[2], r[3])
s = sorted(reqs, key=key)
print("queue: " + " > ".join(r[0] for r in s))
for b in range(1, 4):
    r = s[b - 1]
    print(f"bed {b}: {r[0]} (waited {r[2]} min)")
print(f"still waiting: {len(reqs) - 3}")
print(f"most urgent: {s[0][0]}")
