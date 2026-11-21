import heapq
h = []
for name, pts in [("AXE", 4200), ("BOB", 1500), ("CAT", 8800), ("DEX", 3100), ("EVE", 2600), ("FOX", 1200), ("GUS", 9900), ("HAL", 3100), ("JO", 7000)]:
    heapq.heappush(h, (pts, name))
    if len(h) > 5:
        o = heapq.heappop(h)
        if o[1] == name: print(f"{name} {pts}: not enough")
        else: print(f"{name} {pts}: in, {o[1]} drops out")
    else: print(f"{name} {pts}: in")
print("HIGH SCORES")
for i, (p, n) in enumerate(sorted(h, reverse=True)): print(f"{i + 1} {n:<4}{p:>6}")
