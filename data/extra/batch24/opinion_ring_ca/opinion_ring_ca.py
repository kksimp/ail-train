def update(xs):
    n = len(xs); out = []
    for i in range(n):
        ones = sum(xs[(i + n + d - 2) % n] for d in range(5))
        out.append(1 if ones >= 3 else 0)
    return out

def blocks(xs):
    n = len(xs)
    return sum(1 for i in range(n) if xs[i] != xs[(i + 1) % n])

seed = 53
xs = []
for i in range(24):
    seed = (seed * 75 + 74) % 65537
    xs.append((seed // 3) % 2)
rnd = 0
while True:
    print(f"round {rnd}: {''.join(map(str, xs))}  yes {sum(xs)}, borders {blocks(xs)}")
    nxt = update(xs)
    if nxt == xs: break
    xs = nxt
    rnd += 1
print(f"settled after {rnd} rounds")
