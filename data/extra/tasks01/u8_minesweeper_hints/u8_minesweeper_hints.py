import sys

lines = [l.strip() for l in sys.stdin.read().split("\n") if l.strip() != ""]
if not lines:
    sys.exit(0)
if any(len(l) != len(lines[0]) or any(c not in "*." for c in l) for l in lines):
    print("invalid field")
    sys.exit(0)
R, C = len(lines), len(lines[0])
mines = 0
for r in range(R):
    out = ""
    for c in range(C):
        if lines[r][c] == "*":
            out += "*"
            mines += 1
            continue
        n = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                rr, cc = r + dr, c + dc
                if (dr or dc) and 0 <= rr < R and 0 <= cc < C and lines[rr][cc] == "*":
                    n += 1
        out += str(n)
    print(out)
print("mines: %d" % mines)
