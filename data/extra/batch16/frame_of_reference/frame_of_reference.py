def bit_width(n):
    w = 0
    while n > 0:
        w += 1
        n >>= 1
    return w

blocks = [[1000, 1003, 1001, 1007, 1002, 1010, 1004, 1006], [5000, 5100, 5050, 5200, 5025, 5075, 5150, 5125], [7, 7, 7, 7, 7, 7, 7, 7], [0, 900000, 12, 5, 77, 1, 3, 2]]
raw_total = 0
packed_total = 0
for blk in blocks:
    base = min(blk)
    top = max(blk)
    width = bit_width(top - base)
    offsets = [v - base for v in blk]
    bits = 64 + 8 + width * len(blk)
    raw = 64 * len(blk)
    raw_total += raw
    packed_total += bits
    print(f"base {base:>4} width {width:>2} offsets {offsets}: {bits} bits vs {raw}")
pct = packed_total * 100 // raw_total
print(f"total {packed_total} bits vs {raw_total} ({pct}% of raw)")
