o = {"Ari": 0, "Bo": 0, "Cy": 0}; I = [("milk", 189, ["Ari", "Bo", "Cy"]), ("coffee", 650, ["Ari", "Cy"]), ("bread", 145, ["Ari", "Bo", "Cy"]), ("cereal", 299, ["Bo"]), ("cheese", 410, ["Ari", "Bo", "Cy"])]
for n, c, w in I:
    for i, p in enumerate(w): o[p] += c // len(w) + (1 if i < c % len(w) else 0)
t = sum(i[1] for i in I)
for p in o: print(f"{p}: {o[p] // 100}.{o[p] % 100:02}")
print(f"total {t // 100}.{t % 100:02}, shares add up: {'true' if sum(o.values()) == t else 'false'}")
