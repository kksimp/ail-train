def home(key):
    return sum(ord(c) for c in key) % 5

down = {2}
stored = {}
hints = {}
for key in ["cart:7", "user:42", "img:9", "sess:x"]:
    start = home(key)
    wanted = [(start + k) % 5 for k in range(3)]
    placed = []
    missing = [w for w in wanted if w in down]
    step = 0
    while len(placed) < 3 and step < 5:
        node = (start + step) % 5
        step += 1
        if node in down:
            continue
        if node in wanted:
            stored.setdefault(node, []).append(key)
            placed.append(f"n{node}")
        elif missing:
            owner = missing.pop()
            hints.setdefault(node, []).append(f"{key}>n{owner}")
            placed.append(f"n{node}(hint for n{owner})")
    print(f"{key:<8} home n{start}: {' '.join(placed)}")
down.remove(2)
print("n2 recovers")
for node, hs in hints.items():
    for h in hs:
        parts = h.split(">n")
        owner = int(parts[1])
        stored.setdefault(owner, []).append(parts[0])
        print(f"  n{node} hands {parts[0]} to n{owner}")
print(f"n2 now holds: {', '.join(stored.get(2, []))}")
