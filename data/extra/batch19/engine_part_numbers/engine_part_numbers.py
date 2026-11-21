rows = ["31...#.58.", "..*....*..", ".7.55..12.", "......#...", "9..$...4..", "...61.*...", "88.....23."]
g = [list(r) for r in rows]
h = len(g); w = len(g[0])
total = 0; loose = []; stars = {}
for r in range(h):
    c = 0
    while c < w:
        if not g[r][c].isdigit():
            c += 1; continue
        start = c; n = 0
        while c < w and g[r][c].isdigit():
            n = n * 10 + int(g[r][c]); c += 1
        touched = False
        for y in range(max(r - 1, 0), min(r + 2, h)):
            for x in range(max(start - 1, 0), min(c + 1, w)):
                ch = g[y][x]
                if ch != '.' and not ch.isdigit():
                    touched = True
                    if ch == '*':
                        stars.setdefault(y * 100 + x, []).append(n)
        if touched: total += n
        else: loose.append(n)
print(f"numbers with no symbol: {loose}")
print(f"part 1: part numbers sum to {total}")
ratio = 0
for pos, nums in stars.items():
    if len(nums) == 2:
        print(f"  gear at row {pos // 100} col {pos % 100}: {nums[0]} x {nums[1]}")
        ratio += nums[0] * nums[1]
print(f"part 2: gear ratios sum to {ratio}")
