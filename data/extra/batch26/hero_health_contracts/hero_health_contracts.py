hp, mx = 100, 100
for k, n in [("hit", 30), ("hit", 25), ("heal", 40), ("hit", 70), ("heal", 100), ("hit", 120)]:
    if k == "hit":
        hp = max(hp - n, 0)
        print(f"Wren takes {n}: {hp}/{mx}")
    else:
        b = hp; hp = min(hp + n, mx)
        print(f"Wren drinks a {n} potion, gains {hp - b}: {hp}/{mx}")
print(f"Wren is {'knocked out' if hp == 0 else 'standing'}")
