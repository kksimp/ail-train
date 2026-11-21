def pow9(e):
    return 9 ** e

def count_upto(n):
    ds = [int(c) for c in str(n)]
    size = len(ds)
    total = 0
    for l in range(1, size):
        total += pow9(l)
    prev = -1
    for i in range(size):
        low = 1 if i == 0 else 0
        for d in range(low, ds[i]):
            if d != prev:
                total += pow9(size - i - 1)
        if ds[i] == prev:
            return total
        prev = ds[i]
    return total + 1

def brute(n):
    count = 0
    for x in range(1, n + 1):
        s = str(x)
        ok = True
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                ok = False
        if ok:
            count += 1
    return count

for n in [100, 1000, 2024, 4554, 99999, 1234567890]:
    print(f"1..{n}: {count_upto(n)} numbers with no repeated neighbour digits")
print(f"check by brute force up to 4554: {brute(4554)}")
