def fp(g):
    n = len(g)
    for r in range(n):
        if len(g[r]) != n: return f"row {r + 1} has {len(g[r])} cells"
        if len(set(g[r])) != n: return f"row {r + 1} repeats a symbol"
    for c in range(n):
        seen = set()
        for r in range(n):
            ch = g[r][c]
            if ch in seen: return f"column {c + 1} repeats '{ch}'"
            seen.add(ch)
    return None
cyc = lambda n: ["".join("ABCDEFGHIJ"[(r + c) % n] for c in range(n)) for r in range(n)]
for g in [["ABC", "BCA", "CAB"], ["ABC", "BAC", "CAB"], ["AB", "AB"], ["ABCD", "BCDA", "CD", "DABC"], cyc(5)]:
    print(f"{'/'.join(g)}: {fp(g) or 'latin square'}")
