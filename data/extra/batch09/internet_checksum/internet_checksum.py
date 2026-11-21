def words(h):
    return [int(w, 16) for w in h.split(" ")]

def fold_sum(ws):
    s = 0
    for w in ws:
        s += w
    while s > 65535:
        s = (s & 65535) + (s >> 16)
    return s

header = "4500 0073 0000 4000 4011 0000 c0a8 0001 c0a8 00c7"
ws = words(header)
raw = sum(ws)
folded = fold_sum(ws)
check = 65535 - folded
print(f"raw sum {raw:x}, folded {folded:x}, checksum {check:04x}")
ws[5] = check
print(f"with checksum in place the sum is {fold_sum(ws):x}")
ws[2] = 1
bad = fold_sum(ws)
print(f"after one word changes the sum is {bad:x}, so the header is rejected")
other = words("4500 003c 1c46 4000 4006 0000 ac10 0a63 ac10 0a0c")
print(f"second header checksum {65535 - fold_sum(other):04x}")
