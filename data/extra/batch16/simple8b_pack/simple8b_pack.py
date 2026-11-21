LAYOUTS = [[60, 1], [30, 2], [20, 3], [15, 4], [12, 5], [10, 6], [8, 7], [7, 8], [6, 10], [5, 12], [4, 15], [3, 20], [2, 30], [1, 60]]

def pack(values):
    words = []
    i = 0
    while i < len(values):
        for sel, lay in enumerate(LAYOUTS):
            take = min(lay[0], len(values) - i)
            limit = 1 << lay[1]
            if all(v < limit for v in values[i:i + take]):
                word = 0
                for k in range(take):
                    word |= values[i + k] << (k * lay[1])
                words.append([sel, take, word])
                i += take
                break
    return words

def unpack(words):
    out = []
    for w in words:
        bits = LAYOUTS[w[0]][1]
        mask = (1 << bits) - 1
        for k in range(w[1]):
            out.append((w[2] >> (k * bits)) & mask)
    return out

values = [i % 2 for i in range(30)]
values += [5, 9, 12, 3, 7, 15, 2, 8, 11, 4, 6, 1, 13, 14, 10]
values += [1000, 70000, 3, 5, 123456789]
words = pack(values)
for w in words:
    lay = LAYOUTS[w[0]]
    print(f"selector {w[0]:>2}: {w[1]:>2} values x {lay[1]:>2} bits, payload {w[2]:x}")
same = "true" if unpack(words) == values else "false"
print(f"{len(values)} values in {len(words)} words ({len(words) * 64} bits), round trip {same}")
