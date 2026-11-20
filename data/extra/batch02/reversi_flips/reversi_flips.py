D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
board = ["........", "........", "...W....", "...WB...", "...BW...", "..W.....", "........", "........"]
def at(r, c): return board[r][c] if 0 <= r < 8 and 0 <= c < 8 else " "
def flips(r, c, me):
    if at(r, c) != ".": return 0
    them = "W" if me == "B" else "B"; t = 0
    for dr, dc in D:
        k = 1
        while at(r + dr * k, c + dc * k) == them: k += 1
        if k > 1 and at(r + dr * k, c + dc * k) == me: t += k - 1
    return t
for me in "BW":
    mv = [(flips(r, c, me), r, c) for r in range(8) for c in range(8) if flips(r, c, me) > 0]
    print(f"{me} can play {len(mv)}: " + " ".join(f"{chr(97 + c)}{r + 1}:{n}" for n, r, c in mv))
    if mv:
        n, r, c = sorted(mv, key=lambda m: (-m[0], m[1], m[2]))[0]
        print(f"  best: {chr(97 + c)}{r + 1} flips {n}")
