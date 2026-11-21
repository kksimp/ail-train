C = [200, 100, 50, 20, 10, 5]; S = {200: 1, 100: 2, 50: 1, 20: 3, 10: 2, 5: 4}
for p, pd in [(150, 500), (85, 100), (65, 200), (120, 200), (35, 100), (45, 50)]:
    d = pd - p; g = []; t = dict(S)
    for c in C:
        n = 0
        while d >= c and t[c] > 0: d -= c; t[c] -= 1; n += 1
        if n: g.append((c, n))
    if d == 0: S = t; print(f"price {p} paid {pd}: change {pd - p} = " + " ".join(f"{n}x{c}" for c, n in g))
    else: print(f"price {p} paid {pd}: no exact change, refused")
print("stock " + " ".join(f"{c}:{S[c]}" for c in C))
