def push(h, v):
    h.append(v); i = len(h) - 1
    while i > 0:
        p = (i - 1) // 2
        if h[p] <= h[i]: break
        h[i], h[p] = h[p], h[i]; i = p
def pop(h):
    top = h[0]; last = h.pop()
    if not h: return top
    h[0] = last; i = 0
    while True:
        l = 2 * i + 1; r = l + 1; s = i
        if l < len(h) and h[l] < h[s]: s = l
        if r < len(h) and h[r] < h[s]: s = r
        if s == i: break
        h[i], h[s] = h[s], h[i]; i = s
    return top
ns = [42, 7, 19, 3, 88, 25, 7, 61, 14, 0, 33]
h = []
for n in ns: push(h, n)
print(f"heap array: {h}")
out = []
while h: out.append(pop(h))
print(f"sorted: {out}")
print(f"matches sort: {str(out == sorted(ns)).lower()}")
