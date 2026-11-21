def place(k, n, seq, first):
    if k == 0:
        if len(first) == 0:
            first.append(" ".join(str(x) for x in seq))
        return 1
    count = 0
    size = 2 * n
    last = size - k - 1
    for i in range(0, last):
        if seq[i] == 0 and seq[i + k + 1] == 0:
            seq[i] = k
            seq[i + k + 1] = k
            count += place(k - 1, n, seq, first)
            seq[i] = 0
            seq[i + k + 1] = 0
    return count

for n in range(3, 9):
    seq = [0] * (2 * n)
    first = []
    found = place(n, n, seq, first)
    example = first[0] if len(first) > 0 else "none"
    print(f"n = {n}: {found // 2} pairings (up to reversal), e.g. {example}")
