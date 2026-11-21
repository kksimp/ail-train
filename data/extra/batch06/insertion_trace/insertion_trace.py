x = [7, 3, 9, 1, 6, 2, 8]; s = 0
for i in range(1, len(x)):
    k = x[i]; j = i - 1
    while j >= 0 and x[j] > k: x[j + 1] = x[j]; s += 1; j -= 1
    x[j + 1] = k; print(f"insert {k}: {' '.join(map(str, x))}")
print(f"{s} shifts")
