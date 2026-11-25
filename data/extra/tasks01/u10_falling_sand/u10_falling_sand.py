import sys
lines = sys.stdin.read().split("\n")
head = lines[0].strip() if lines else ""
if not (head.isdigit() and head.isascii()):
    print("error: bad steps"); sys.exit(0)
n = int(head)
g = [list(l) for l in lines[1:] if l != ""]
R = len(g)
for _ in range(n):
    for r in range(R - 2, -1, -1):
        for c in range(len(g[r])):
            if g[r][c] != "o":
                continue
            for dc in (0, -1, 1):
                nc = c + dc
                if 0 <= nc < len(g[r]) and g[r + 1][nc] == ".":
                    g[r][c] = "."; g[r + 1][nc] = "o"
                    break
for row in g:
    print("".join(row))
print("sand", sum(row.count("o") for row in g))
