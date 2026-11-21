from collections import Counter
def shared(a, b):
    keep = []; diff = 0
    for x, y in zip(a, b):
        if x == y: keep.append(x)
        else: diff += 1
    return "".join(keep) if diff == 1 else None

tags = ["kqbrvxa", "mmzrtuu", "pqlaapl", "kqbrwxa", "zzytopz", "hhjjkkl", "abcdefg", "ttrrrsq"]
twos = threes = 0
for t in tags:
    counts = Counter(t).values()
    if 2 in counts: twos += 1
    if 3 in counts: threes += 1
print(f"{twos} tags with a pair, {threes} with a triple")
print(f"part 1: checksum {twos * threes}")
for i in range(len(tags)):
    for j in range(i + 1, len(tags)):
        s = shared(tags[i], tags[j])
        if s is not None:
            print(f"part 2: {tags[i]} and {tags[j]} share {s}")
