import sys

lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
size = 0
strat = ""
if lines:
    f = lines[0].split()
    if len(f) == 4 and f[0] == "memory" and f[2] == "strategy" and f[3] in ("first", "best"):
        try:
            size = int(f[1])
            strat = f[3]
        except ValueError:
            size = 0
if size < 1:
    print("bad header")
    sys.exit(0)
blocks = [[0, size, ""]]
out = []
for l in lines[1:]:
    f = l.split()
    if len(f) == 3 and f[0] == "alloc" and f[2].lstrip("-").isdigit() and int(f[2]) >= 1:
        name, n = f[1], int(f[2])
        if any(b[2] == name for b in blocks):
            out.append(f"alloc {name} {n} -> exists")
            continue
        pick = -1
        for i, b in enumerate(blocks):
            if b[2] == "" and b[1] >= n:
                if strat == "first":
                    pick = i
                    break
                if pick < 0 or b[1] < blocks[pick][1]:
                    pick = i
        if pick < 0:
            out.append(f"alloc {name} {n} -> fail")
            continue
        b = blocks[pick]
        addr = b[0]
        if b[1] > n:
            blocks.insert(pick + 1, [addr + n, b[1] - n, ""])
        b[1] = n
        b[2] = name
        out.append(f"alloc {name} {n} -> {addr}")
    elif len(f) == 2 and f[0] == "free":
        idx = [i for i, b in enumerate(blocks) if b[2] == f[1]]
        if not idx:
            out.append(f"free {f[1]} -> unknown")
            continue
        blocks[idx[0]][2] = ""
        i = 0
        while i + 1 < len(blocks):
            if blocks[i][2] == "" and blocks[i + 1][2] == "":
                blocks[i][1] += blocks[i + 1][1]
                blocks.pop(i + 1)
            else:
                i += 1
        out.append(f"free {f[1]} -> ok")
    else:
        out.append(f"? {l}")
out.append("layout")
big = 0
for s, n, name in blocks:
    out.append(f"{s}-{s + n - 1} {name or 'free'}")
    if name == "":
        big = max(big, n)
out.append(f"largest free={big}")
print("\n".join(out))
