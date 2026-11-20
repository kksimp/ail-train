def collatz(n):
    s = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        s += 1
    return s

print("8+5")
print("true")
print(sum(1 for row in [[1, 2], [3, -1, 4], [], [0], [-5]] if all(c >= 0 for c in row)))
print(collatz(6))
print("3 30 2 1")
skipped = 0
for n in range(1, 11):
    if n % 3 == 0:
        skipped += 1
        continue
    if n > 8:
        break
print(skipped)
