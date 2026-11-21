def by_blocks(n, blocks):
    total = 0
    i = 1
    while i <= n:
        q = n // i
        j = n // q
        total += q * (j - i + 1)
        blocks[0] += 1
        i = j + 1
    return total

def brute(n):
    total = 0
    for i in range(1, n + 1):
        total += n // i
    return total

for n in [10, 100, 1000, 100000, 1000000000]:
    blocks = [0]
    fast = by_blocks(n, blocks)
    slow = f"{brute(n)}" if n <= 100000 else "skipped"
    print(f"N = {n:>10}: sum {fast:>11} in {blocks[0]:>5} blocks (one by one: {slow})")
counts = []
for k in range(1, 13):
    b = [0]
    counts.append(by_blocks(k, b) - by_blocks(k - 1, b))
print(f"divisor counts d(1..12) as differences: {counts}")
