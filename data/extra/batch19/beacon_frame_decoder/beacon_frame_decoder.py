def decode(hx):
    bits = []
    for c in hx:
        d = int(c, 16)
        for k in [3, 2, 1, 0]:
            bits.append((d >> k) & 1)
    pos = [0]; versions = [0]
    def read(n):
        v = 0
        for _ in range(n):
            v = v * 2 + bits[pos[0]]; pos[0] += 1
        return v
    def packet():
        versions[0] += read(2)
        kind = read(2)
        if kind == 0:
            return read(8)
        count = read(3)
        vals = [packet() for i in range(count)]
        if kind == 1: return sum(vals)
        if kind == 2:
            p = 1
            for v in vals: p *= v
            return p
        return max(vals)
    value = packet()
    return [versions[0], value, pos[0]]

for frame in ["9680BC800E011DE0480120D8", "642901901E00C", "4A0"]:
    r = decode(frame)
    print(f"{frame}: {r[2]} bits used")
    print(f"  part 1 version sum {r[0]}, part 2 value {r[1]}")
