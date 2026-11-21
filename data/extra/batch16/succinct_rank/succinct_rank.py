def rank(bits, blocks, i):
    r = blocks[i // 8]
    for k in range(i // 8 * 8, i):
        r += bits[k]
    return r

def select1(bits, blocks, k):
    lo, hi = 0, len(bits)
    while lo < hi:
        mid = (lo + hi) // 2
        if rank(bits, blocks, mid + 1) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo

text = "101100111000101101101111000010100011101111011001"
bits = [int(c) for c in text]
blocks = [0]
for b in range(len(bits) // 8):
    blocks.append(blocks[b] + sum(bits[b * 8:b * 8 + 8]))
print(f"{len(bits)} bits, block counts {blocks}")
for i in [0, 5, 8, 21, 33, 48]:
    brute = sum(bits[0:i])
    print(f"rank({i:>2}) = {rank(bits, blocks, i):>2} ones before it (scan {brute})")
for k in [1, 7, 15, 26]:
    pos = select1(bits, blocks, k)
    print(f"select1({k:>2}) = position {pos:>2}, bit there is {bits[pos]}")
