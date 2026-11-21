chargers = [4, 1, 7, 10, 5, 13, 2, 8, 11, 16, 14, 6, 17, 19]
chain = [0] + sorted(chargers)
device = chain[-1] + 3
chain.append(device)
gaps = {}
for a, b in zip(chain, chain[1:]):
    gaps[b - a] = gaps.get(b - a, 0) + 1
print(f"steps of 1: {gaps.get(1, 0)}, of 2: {gaps.get(2, 0)}, of 3: {gaps.get(3, 0)}")
print(f"part 1: {gaps.get(1, 0) * gaps.get(3, 0)}")
ways = {0: 1}
for v in chain[1:]:
    ways[v] = ways.get(v - 1, 0) + ways.get(v - 2, 0) + ways.get(v - 3, 0)
print(f"part 2: {ways[device]} possible chains")
