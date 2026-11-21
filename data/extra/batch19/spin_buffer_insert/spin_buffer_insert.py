step = 7
buf = [0]; pos = 0
for v in range(1, 601):
    pos = (pos + step) % len(buf) + 1
    buf.insert(pos, v)
print(f"first values: {buf[:8]}")
print(f"part 1: after 600 comes {buf[(pos + 1) % len(buf)]}")
p = 0; after_zero = 0
for v in range(1, 60001):
    p = (p + step) % v + 1
    if p == 1: after_zero = v
print(f"part 2: after 0 comes {after_zero}")
