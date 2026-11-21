def blow(h):
    out = list(h)
    last = len(h) - 1
    for i in range(last):
        if h[i] - h[i+1] >= 2:
            out[i] -= 1
            out[i+1] += 1
    if h[last] >= 2:
        out[last] -= 1
    return out

h = [9, 9, 9, 9, 9, 9, 0, 0, 0, 0]
start = sum(h)
print(f"step  0: {''.join(map(str, h))}")
steps = 0
while True:
    nxt = blow(h)
    if nxt == h: break
    h = nxt
    steps += 1
    if steps % 3 == 0:
        print(f"step {steps:>2}: {''.join(map(str, h))}")
print(f"rests after {steps} steps: {''.join(map(str, h))}")
print(f"grains lost off the edge: {start - sum(h)}")
