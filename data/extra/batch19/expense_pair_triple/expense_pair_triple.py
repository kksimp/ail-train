def pair(xs, target):
    seen = set()
    for x in xs:
        if target - x in seen:
            return [target - x, x]
        seen.add(x)
    return []

receipts = [412, 977, 260, 1188, 655, 89, 523, 741, 336, 870, 104, 1311]
target = 1500
two = pair(receipts, target)
print(f"pair: {two[0]} + {two[1]} = {target}")
print(f"part 1: product {two[0] * two[1]}")
for i, x in enumerate(receipts):
    rest = pair(receipts[i + 1:], target - x)
    if rest:
        print(f"triple: {x} + {rest[0]} + {rest[1]} = {target}")
        print(f"part 2: product {x * rest[0] * rest[1]}")
        break
