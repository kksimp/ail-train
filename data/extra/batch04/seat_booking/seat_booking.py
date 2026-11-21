R, S = 5, 8; fr = [[True] * S for _ in range(R)]
for r, s in [(2, 3), (2, 4), (1, 0), (3, 5)]: fr[r][s] = False
def fb(n):
    b = None; bs = 10 ** 6
    for r in range(R):
        for s in range(S - n + 1):
            if all(fr[r][k] for k in range(s, s + n)):
                sc = abs(2 * r - (R - 1)) * 100 + abs(2 * s + n - 1 - (S - 1))
                if sc < bs: bs = sc; b = (r, s)
    return b
for n in [2, 4, 3, 8, 6]:
    b = fb(n)
    if b:
        r, s = b
        for k in range(s, s + n): fr[r][k] = False
        print(f"{n} seats: row {'ABCDE'[r]}, seats {s + 1}-{s + n}")
    else: print(f"{n} seats: no block free")
for r in range(R): print("".join("." if f else "x" for f in fr[r]))
