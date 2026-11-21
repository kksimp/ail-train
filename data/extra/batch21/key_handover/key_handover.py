holder = {"front": "safe", "back": "safe", "garage": "Omar", "shed": "Omar", "spare": "safe"}
moves = [("front", "safe", "Lena"), ("back", "Lena", "Pete"), ("back", "safe", "Pete"), ("garage", "Omar", "Lena"), ("loft", "Omar", "Pete"), ("shed", "Omar", "Lena"), ("front", "Lena", "safe"), ("spare", "safe", "Lena")]
refused = 0
for key, f, t in moves:
    if key not in holder:
        refused += 1
        print(f"refused: no such key: {key}")
        continue
    cur = holder[key]
    if cur != f:
        refused += 1
        print(f"refused: {f} cannot give the {key} key, {cur} has it")
        continue
    holder[key] = t
    n = sum(1 for w in holder.values() if w == t)
    print(f"{key} key: {f} -> {t} ({t} now holds {n})")
count = {}
for key, who in holder.items():
    count[who] = count.get(who, 0) + 1
for key, who in holder.items():
    print(f"{key:<7} {who}")
most = sorted(count.keys(), key=lambda w: -count[w])
print(f"{refused} refused; most keys: {most[0]} with {count[most[0]]}")
