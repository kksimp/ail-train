N = {"maths": 6, "history": 4, "biology": 5}; E = {"maths": 5, "history": 3, "biology": 6}
for d in range(1, 7):
    o = [s for s in N if N[s] > 0 and E[s] > d - 1]
    if not o: print(f"day {d}: rest"); continue
    p = min(o, key=lambda s: (E[s], s)); h = min(N[p], 2); N[p] -= h; print(f"day {d}: {p} {h}h (left {N[p]})")
for s in ["maths", "history", "biology"]: print(f"{s}: {'ready' if N[s] == 0 else 'short'}")
