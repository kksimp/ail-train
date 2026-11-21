def next_state(s, taps, width):
    fb = 0
    for t in taps:
        fb = fb ^ ((s >> (width - t)) & 1)
    return (s >> 1) | (fb << (width - 1))

def period(start, taps, width):
    s = next_state(start, taps, width)
    n = 1
    while s != start:
        s = next_state(s, taps, width)
        n += 1
    return n

s = 1
states = []
out_bits = []
for _ in range(15):
    states.append(str(s))
    out_bits.append(str(s & 1))
    s = next_state(s, [4, 3], 4)
print(f"4-bit taps 4,3 states: {' '.join(states)}")
print(f"output bits: {''.join(out_bits)}")
for w, taps in [(4, [4, 3]), (4, [4, 2]), (5, [5, 3]), (5, [5, 4]), (8, [8, 6, 5, 4])]:
    p = period(1, taps, w)
    full = (1 << w) - 1
    kind = "maximal" if p == full else "short"
    print(f"width {w} taps {taps}: period {p} of {full} ({kind})")
