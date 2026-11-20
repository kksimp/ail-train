players = [("cy", 70, 31), ("ann", 90, 25), ("bob", 70, 44), ("dee", 85, 25)]

def names(ps):
    return " ".join(p[0] for p in ps)

for i, p in enumerate(sorted(players, key=lambda p: (-p[1], p[0]))):
    print(f"{i + 1}. {p[0]} {p[1]}")
print(names(sorted(players, key=lambda p: p[2])))
print(names(reversed(sorted(players, key=lambda p: p[0]))))
print(names(sorted(players, key=lambda p: (p[2], -p[1]))))
print(names(players))
print(min(players, key=lambda p: p[2])[0])
words = ["pear", "fig", "banana", "kiwi"]
print(" ".join(sorted(words, key=len)))
print(" ".join(sorted(words)))
print("3 2 1")
