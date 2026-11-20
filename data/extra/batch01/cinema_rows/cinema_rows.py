W = 10
hall = [0b0000110000, 0, 0b1111111111, 0]
def fr(row, k):
    for s in range(W - k + 1):
        if row & (((1 << k) - 1) << s) == 0: return s
    return None
for k in [4, 5, 2, 7, 3, 9]:
    for r in range(len(hall)):
        s = fr(hall[r], k)
        if s is not None:
            hall[r] |= ((1 << k) - 1) << s
            print(f"party of {k}: row {r + 1}, seats {s + 1}-{s + k}")
            break
    else:
        print(f"party of {k}: no room")
for i, row in enumerate(hall):
    print(f"row {i + 1} " + "".join("X" if row & (1 << j) else "." for j in range(W)))
