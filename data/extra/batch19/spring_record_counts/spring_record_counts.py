def ways(s, runs, i, j, memo):
    if i >= len(s):
        return 1 if j == len(runs) else 0
    key = i * 100 + j
    if key in memo: return memo[key]
    total = 0
    if s[i] != '#':
        total += ways(s, runs, i + 1, j, memo)
    if s[i] != '.' and j < len(runs):
        g = runs[j]
        fits = i + g <= len(s) and '.' not in s[i:i + g]
        if fits and (i + g == len(s) or s[i + g] != '#'):
            total += ways(s, runs, i + g + 1, j + 1, memo)
    memo[key] = total
    return total

def count(row, copies):
    a, b = row.split(" ")
    s = list("?".join([a] * copies))
    runs = [int(t) for t in ",".join([b] * copies).split(",")]
    return ways(s, runs, 0, 0, {})

rows = ["#.??.### 1,1,3", "?#?#?#?#? 1,3,1", "??..??...?##. 1,1,3", ".??..#??.## 1,2,2", "?###???????? 3,2,1", "??.?#?.?? 1,2"]
p1 = p2 = 0
for r in rows:
    a = count(r, 1); b = count(r, 3)
    print(f"{r:<22} {a:>3} {b:>7}")
    p1 += a; p2 += b
print(f"part 1: {p1} layouts")
print(f"part 2: {p2} layouts when unfolded")
