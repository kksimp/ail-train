def encode(ids, universe, lows, highs):
    n = len(ids)
    l = 0
    while (n << (l + 1)) <= universe:
        l += 1
    size = n + (universe >> l) + 1
    highs.extend([0] * size)
    for i in range(n):
        lows.append(ids[i] & ((1 << l) - 1))
        highs[(ids[i] >> l) + i] = 1
    return l

def access(lows, highs, l, i):
    seen = -1
    pos = 0
    while seen < i:
        if highs[pos] == 1:
            seen += 1
        pos += 1
    high = pos - 1 - i
    return (high << l) | lows[i]

ids = [3, 9, 14, 22, 23, 41, 57, 58, 60, 88, 95, 120]
universe = 128
lows = []
highs = []
l = encode(ids, universe, lows, highs)
print(f"{len(ids)} ids below {universe}: low bits per id l = {l}")
print(f"low parts:  {lows}")
shown = "".join(str(x) for x in highs)
print(f"high bits:  {shown}")
total = len(ids) * l + len(highs)
print(f"space: {total} bits, against {len(ids) * 7} bits for plain 7-bit ids")
back = [access(lows, highs, l, i) for i in range(len(ids))]
print(f"decoded:    {back}")
