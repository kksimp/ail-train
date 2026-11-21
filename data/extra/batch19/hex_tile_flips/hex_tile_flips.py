def key(q, r):
    return (q + 100) * 1000 + r + 100

def walk(path):
    q = r = 0; i = 0
    while i < len(path):
        if path[i] == 'e': q += 1
        elif path[i] == 'w': q -= 1
        else:
            two = path[i:i + 2]; i += 1
            if two == "ne": q += 1; r -= 1
            elif two == "nw": r -= 1
            elif two == "se": r += 1
            else: q -= 1; r += 1
        i += 1
    return key(q, r)

def neighbours(k):
    q = k // 1000 - 100; r = k % 1000 - 100
    return [key(q + 1, r), key(q - 1, r), key(q + 1, r - 1), key(q, r - 1), key(q, r + 1), key(q - 1, r + 1)]

paths = ["esenee", "wnwsw", "nwwswee", "seswneswnw", "eee", "nenene", "wwsese", "esenee", "swswne", "neenw", "sesww"]
black = set()
for p in paths:
    black ^= {walk(p)}
print(f"part 1: {len(black)} black tiles")
for day in range(1, 11):
    counts = {}
    for b in black:
        for n in neighbours(b):
            counts[n] = counts.get(n, 0) + 1
    black = {k for k, n in counts.items() if n == 2 or (n == 1 and k in black)}
    if day in (1, 5):
        print(f"day {day}: {len(black)} black tiles")
print(f"part 2: {len(black)} black tiles after 10 days")
