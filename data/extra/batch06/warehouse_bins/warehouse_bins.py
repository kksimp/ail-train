B = []
for p in sorted([12, 31, 8, 22, 45, 17, 9, 26, 14, 30, 5, 19], reverse=True):
    for b in B:
        if sum(b) + p <= 50: b.append(p); break
    else: B.append([p])
w = 0
for i, b in enumerate(B): u = sum(b); w += 50 - u; print(f"bin {i + 1}: {'+'.join(map(str, b))} = {u}/50")
print(f"{len(B)} bins, {w} units empty, lower bound {(238 + 49) // 50}")
