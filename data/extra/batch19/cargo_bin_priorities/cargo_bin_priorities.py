def priority(c):
    return ord(c) - 96 if c.islower() else ord(c) - 38

def best(s):
    return max((priority(c) for c in s), default=0)

bins = ["Kabcdaefgh", "LmnKopqrLs", "tuvwxyzKxB", "QJMtuMoxev", "PvrPzEvGQH", "iFmZiSXFQq"]
part1 = 0
for b in bins:
    half = len(b) // 2
    p = best(set(b[:half]) & set(b[half:]))
    print(f"{b}: shared priority {p}")
    part1 += p
print(f"part 1: {part1}")
part2 = 0
for g in range(len(bins) // 3):
    part2 += best(set(bins[g * 3]) & set(bins[g * 3 + 1]) & set(bins[g * 3 + 2]))
print(f"part 2: {part2}")
