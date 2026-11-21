w = {}
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7): w[a + b + c] = w.get(a + b + c, 0) + 1
for s in range(3, 19): print(f"{s:>2} {w[s]:>2} {'#' * w[s]}")
h = sum(w[s] for s in range(15, 19)); print(f"mean {sum(s * w[s] for s in w) / 216:.2f}, P(sum >= 15) = {h}/216 = {h * 100 / 216:.2f}%")
