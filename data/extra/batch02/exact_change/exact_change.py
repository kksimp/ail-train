jar = [50, 20, 20, 10, 5, 2, 2]
can = [False] * 121; can[0] = True
for c in jar:
    for s in range(120, c - 1, -1):
        if can[s - c]: can[s] = True
imp = [s for s in range(1, 111) if not can[s]]
print(f"cannot pay {len(imp)} amounts, first: " + " ".join(map(str, imp[:8])))
def pick(coins, t):
    if t == 0: return []
    if not coins: return None
    last, rest = coins[-1], coins[:-1]
    if last <= t:
        w = pick(rest, t - last)
        if w is not None: return w + [last]
    return pick(rest, t)
for a in [37, 64, 109, 8]:
    u = pick(jar, a)
    print(f"{a}: {'+'.join(map(str, u))}" if u is not None else f"{a}: impossible")
