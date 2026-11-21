def zigzag(n):
    return 2 * n if n >= 0 else -2 * n - 1

def unzigzag(z):
    return z // 2 if z % 2 == 0 else -((z + 1) // 2)

def encode(v):
    out = []
    while True:
        b = v & 127
        v = v >> 7
        if v != 0:
            out.append(b | 128)
        else:
            out.append(b)
            break
    return out

def decode(bs):
    v = 0
    shift = 0
    for b in bs:
        v = v | ((b & 127) << shift)
        shift += 7
    return v

def hexs(bs):
    return " ".join(f"{b:02x}" for b in bs)

for n in [0, 1, 127, 128, 300, 16384, 1000000]:
    bs = encode(n)
    print(f"{n:>8} -> {hexs(bs):<12} back {decode(bs)}")
for n in [-1, 1, -64, 64, -1000]:
    z = zigzag(n)
    bs = encode(z)
    back = unzigzag(decode(bs))
    print(f"{n:>8} zigzag {z:>4} -> {hexs(bs):<12} back {back}")
