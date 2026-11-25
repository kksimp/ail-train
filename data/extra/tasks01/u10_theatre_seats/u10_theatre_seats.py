import sys
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
i = 0
g = []
while i < len(lines) and lines[i] != "":
    g.append(list(lines[i])); i += 1
k = 0
for l in lines[i + 1:]:
    t = l.strip()
    if t == "":
        continue
    k += 1
    if not (t.isascii() and t.isdigit()) or int(t) < 1:
        print(f"group {k}: invalid"); continue
    s = int(t)
    found = None
    for r, row in enumerate(g):
        run = 0
        for c, ch in enumerate(row):
            run = run + 1 if ch == "." else 0
            if run == s:
                found = (r, c - s + 1); break
        if found:
            break
    if not found:
        print(f"group {k}: none"); continue
    r, a = found
    for c in range(a, a + s):
        g[r][c] = "o"
    print(f"group {k}: row {r} seats {a}-{a + s - 1}")
for row in g:
    print("".join(row))
print("free", sum(row.count(".") for row in g))
