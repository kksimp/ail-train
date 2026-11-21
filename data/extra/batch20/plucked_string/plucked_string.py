def first_step(y0):
    y1 = []
    for i in range(len(y0)):
        if i == 0 or i == len(y0) - 1:
            y1.append(0)
        else:
            y1.append((y0[i - 1] + y0[i + 1]) // 2)
    return y1

def step(prev, cur):
    out = []
    for i in range(len(cur)):
        if i == 0 or i == len(cur) - 1:
            out.append(0)
        else:
            out.append(cur[i - 1] + cur[i + 1] - prev[i])
    return out

y0 = [0, 4, 8, 12, 10, 8, 6, 4, 2, 0]
prev = y0
cur = first_step(y0)
print(f"step  0: {y0}")
for n in range(1, 19):
    if n % 3 == 0:
        print(f"step {n:>2}: {cur}")
    if n == 9:
        mirror = [-y0[len(y0) - 1 - i] for i in range(len(y0))]
        print(f"  the pluck flipped and mirrored: {str(cur == mirror).lower()}")
    if n == 18:
        print(f"  back to the pluck: {str(cur == y0).lower()}")
    nxt = step(prev, cur)
    prev = cur
    cur = nxt
