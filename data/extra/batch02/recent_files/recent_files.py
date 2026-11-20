items, cap = [], 5
for cmd in ["open a.ail", "open b.md", "open c.txt", "open a.ail", "open d.ail", "open e.ail", "open f.ail", "close c.txt", "close zzz", "open b.md"]:
    op, p = cmd.split(" ")
    if op == "open":
        if p in items: items.remove(p)
        items.insert(0, p); del items[cap:]
    elif p in items:
        items.remove(p)
    else:
        print(f"{p} was not open")
    print(f"{cmd:<12} [{' '.join(items)}]")
