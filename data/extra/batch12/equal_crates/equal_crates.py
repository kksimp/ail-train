def place(i, items, target, loads, crate_of):
    if i == len(items):
        return True
    for c in range(len(loads)):
        if loads[c] + items[i] <= target:
            loads[c] += items[i]
            crate_of[i] = c
            if place(i + 1, items, target, loads, crate_of):
                return True
            loads[c] -= items[i]
        if loads[c] == 0:
            break
    return False

def split(weights, k):
    total = sum(weights)
    if total % k != 0:
        return f"{k} crates: impossible, total {total} does not divide"
    items = sorted(weights, reverse=True)
    loads = [0] * k
    crate_of = [-1] * len(items)
    if not place(0, items, total // k, loads, crate_of):
        return f"{k} crates: impossible"
    parts = []
    for c in range(k):
        mine = [items[i] for i in range(len(items)) if crate_of[i] == c]
        parts.append("+".join(str(x) for x in mine))
    return f"{k} crates of {total // k}: {' | '.join(parts)}"

weights = [4, 3, 2, 3, 5, 2, 1, 7, 6, 3]
print(f"parcels {weights}, total {sum(weights)}")
for k in [2, 3, 4, 5, 6, 9]:
    print(split(weights, k))
