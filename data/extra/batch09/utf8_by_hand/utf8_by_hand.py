def encode(cp):
    if cp < 128:
        return [cp]
    if cp < 2048:
        return [192 | (cp >> 6), 128 | (cp & 63)]
    if cp < 65536:
        return [224 | (cp >> 12), 128 | ((cp >> 6) & 63), 128 | (cp & 63)]
    return [240 | (cp >> 18), 128 | ((cp >> 12) & 63), 128 | ((cp >> 6) & 63), 128 | (cp & 63)]

def decode(bs):
    n = len(bs)
    cp = bs[0] if n == 1 else (bs[0] & 31 if n == 2 else (bs[0] & 15 if n == 3 else bs[0] & 7))
    for i in range(1, n):
        cp = (cp << 6) | (bs[i] & 63)
    return cp

agree = 0
points = [65, 233, 223, 1046, 8364, 20013, 119070]
for cp in points:
    bs = encode(cp)
    mine = " ".join(f"{b:02x}" for b in bs)
    theirs = chr(cp).encode("utf-8").hex(" ")
    if mine == theirs:
        agree += 1
    h = f"{cp:04x}".upper()
    print(f"U+{h:<6} {len(bs)} bytes: {mine:<12} back U+{decode(bs):04x}")
print(f"{agree} of {len(points)} match the built-in encoder")
