t = "a quick movement of the enemy will jeopardise six gunboats"
c = {}
for ch in t:
    if ch.isalpha(): c[ch] = c.get(ch, 0) + 1
V = "aeiou"; top = max(c.get(v, 0) for v in V)
for lv in range(top, 0, -1):
    print(f"{lv:>2}" + "".join(" " + ("#" if c.get(v, 0) >= lv else " ") for v in V))
print("   " + " ".join(V))
print(f"missing letters: {sum(1 for x in 'abcdefghijklmnopqrstuvwxyz' if x not in c)}")
