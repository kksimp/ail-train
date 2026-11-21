E = [("sprint", ["red", "blue", "green"]), ("relay", ["blue", "green", "red"]), ("long jump", ["green", "red", "yellow"]), ("high jump", ["blue", "yellow", "green"]), ("egg race", ["yellow", "blue", "red"])]
A = [5, 3, 1]; t = {}; be = {}
for n, pl in E:
    for i, h in enumerate(pl):
        t[h] = t.get(h, 0) + A[i]
        if A[i] > be.get(h, ("", 0))[1]: be[h] = (n, A[i])
for i, h in enumerate(sorted(t, key=lambda h: (-t[h], h))): print(f"{i + 1}. {h:<7} {t[h]:>2}  best: {be[h][0]}")
