ps = [("basil", [12, 20, 31, 40, 52]), ("chili", [8, 9, 9, 15, 24]), ("mint", [15, 28, 35, 41, 44]), ("dill", [10, 18, 17, 25, 37])]
gr = lambda h: [h[i] - h[i - 1] for i in range(1, len(h))]
for n, h in ps:
    g = gr(h); t = max(g)
    print(f"{n:<6} +{h[-1] - h[0]} mm, best week {g.index(t) + 1} (+{t})")
print("grew every week: " + ", ".join(n for n, h in ps if all(x > 0 for x in gr(h))))
