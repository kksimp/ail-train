import re
import sys

VALUES = {}
for letters, v in (("AEILNORSTU", 1), ("DG", 2), ("BCMP", 3), ("FHVWY", 4), ("K", 5), ("JX", 8), ("QZ", 10)):
    for ch in letters:
        VALUES[ch] = v

EDGE = (1, 8, 15)
DIAG = (2, 3, 4, 5, 8, 11, 12, 13, 14)
LAT = (2, 6, 10, 14)


def premium(r, c):
    if r in EDGE and c in EDGE and not (r == 8 and c == 8):
        return "TW"
    if r in DIAG and (r == c or r + c == 16):
        return "DW"
    if r in LAT and c in LAT:
        return "TL"
    if (r in EDGE and c in (4, 12)) or (c in EDGE and r in (4, 12)):
        return "DL"
    return ""


board = {}
total = 0
moves = 0
for line in sys.stdin.read().splitlines():
    f = line.split()
    if not f:
        continue
    text = " ".join(f)
    if (
        len(f) != 4
        or not re.fullmatch(r"[0-9]{1,3}", f[1])
        or not re.fullmatch(r"[0-9]{1,3}", f[2])
        or f[3] not in ("H", "V")
        or not re.fullmatch(r"[A-Z]+", f[0])
    ):
        print(f"{text}: rejected (bad format)")
        continue
    word, row, col, d = f[0], int(f[1]), int(f[2]), f[3]
    cells = [(row, col + i) if d == "H" else (row + i, col) for i in range(len(word))]
    if row < 1 or col < 1 or cells[-1][0] > 15 or cells[-1][1] > 15:
        print(f"{text}: rejected (out of bounds)")
        continue
    total_sq = 0
    mult = 1
    fresh = 0
    err = None
    for ch, (r, c) in zip(word, cells):
        have = board.get((r, c))
        if have is not None and have != ch:
            err = f"conflict at {r} {c}"
            break
        v = VALUES[ch]
        if have is not None:
            total_sq += v
            continue
        fresh += 1
        p = premium(r, c)
        if p == "TW":
            mult *= 3
            total_sq += v
        elif p == "DW":
            mult *= 2
            total_sq += v
        elif p == "TL":
            total_sq += 3 * v
        elif p == "DL":
            total_sq += 2 * v
        else:
            total_sq += v
    if err is None and fresh == 0:
        err = "no new tiles"
    if err:
        print(f"{text}: rejected ({err})")
        continue
    pts = total_sq * mult + (50 if fresh == 7 else 0)
    for ch, pos in zip(word, cells):
        board[pos] = ch
    total += pts
    moves += 1
    print(f"{text}: {pts}")
print(f"total={total} moves={moves}")
