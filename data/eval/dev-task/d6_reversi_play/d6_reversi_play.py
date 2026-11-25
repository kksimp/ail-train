import sys

lines = sys.stdin.read().splitlines()
first = lines[0].strip() if lines else ""
if first not in ("B", "W"):
    print("invalid player")
    sys.exit(0)
grid = []
ok = len(lines) >= 9
if ok:
    for k in range(1, 9):
        row = list(lines[k].strip())
        if len(row) != 8 or any(c not in ".BW" for c in row):
            ok = False
            break
        grid.append(row)
if not ok:
    print("invalid board")
    sys.exit(0)

turn = first


def flips(cell):
    if len(cell) != 2 or not ("a" <= cell[0] <= "h") or not ("1" <= cell[1] <= "8"):
        return "bad cell"
    c = ord(cell[0]) - 97
    r = ord(cell[1]) - 49
    if grid[r][c] != ".":
        return "occupied"
    out = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            y, x = r + dr, c + dc
            run = []
            while 0 <= y < 8 and 0 <= x < 8:
                if grid[y][x] == turn:
                    out.extend(run)
                    break
                if grid[y][x] == ".":
                    break
                run.append((y, x))
                y += dr
                x += dc
    if not out:
        return "no flips"
    return sorted(out)


for raw in lines[9:]:
    cell = raw.strip()
    if not cell:
        continue
    res = flips(cell)
    if isinstance(res, str):
        print(f"{cell} {turn}: illegal ({res})")
        continue
    c = ord(cell[0]) - 97
    r = ord(cell[1]) - 49
    grid[r][c] = turn
    for y, x in res:
        grid[y][x] = turn
    names = " ".join(chr(97 + x) + str(y + 1) for y, x in res)
    print(f"{cell} {turn}: flipped {len(res)}: {names}")
    turn = "W" if turn == "B" else "B"

for row in grid:
    print("".join(row))
flat = [c for row in grid for c in row]
print(f"B={flat.count('B')} W={flat.count('W')} next={turn}")
