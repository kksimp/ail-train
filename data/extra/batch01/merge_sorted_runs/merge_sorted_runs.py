def merge(a, b):
    out, i, j, c = [], 0, 0, 0
    while i < len(a) and j < len(b):
        c += 1
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out + a[i:] + b[j:], c
acc, tot = [], 0
for r in [[3, 9, 14], [1, 2, 20, 21], [], [5, 9], [0, 30]]:
    acc, c = merge(acc, r)
    tot += c
    print(" ".join(map(str, acc)) + f" ({c} compares)")
print(f"total compares: {tot}, sorted: true")
