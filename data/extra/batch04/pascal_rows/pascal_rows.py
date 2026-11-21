r = [1]
for n in range(9):
    t = ' '.join(map(str, r)); print(" " * ((40 - len(t)) // 2) + t); r = [1] + [r[i - 1] + r[i] for i in range(1, len(r))] + [1]
print(f"row 9 middle: {r[4]}")
