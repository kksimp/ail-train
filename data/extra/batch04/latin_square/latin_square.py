def bd(n): return [[(r + c) % n + 1 for c in range(n)] for r in range(n)]
def il(s):
    n = len(s); w = list(range(1, n + 1))
    return all(sorted(s[i]) == w and sorted(s[r][i] for r in range(n)) == w for i in range(n))
s = bd(5)
for r in s: print(" ".join(map(str, r)))
print(f"latin: {'true' if il(s) else 'false'}"); b = bd(4); b[2] = [1, 2, 3, 4]; print(f"broken latin: {'true' if il(b) else 'false'}")
