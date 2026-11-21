f = ["*...*", ".....", "..*..", "**...", "....*"]
def an(g):
    out = []
    for r in range(len(g)):
        line = ""
        for c in range(len(g[r])):
            if g[r][c] == "*": line += "*"; continue
            n = sum(1 for rr in range(max(r - 1, 0), min(r + 1, len(g) - 1) + 1) for cc in range(max(c - 1, 0), min(c + 1, len(g[r]) - 1) + 1) if g[rr][cc] == "*")
            line += "." if n == 0 else str(n)
        out.append(line)
    return out
b = an(f)
for i in range(len(f)): print(f"{f[i]}   {b[i]}")
print(f"mines: {sum(r.count('*') for r in f)}")
