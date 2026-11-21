state = 23
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def fill(h, a, b, spread):
    if b - a < 2: return
    m = (a + b) // 2
    offset = below(2 * spread + 1) - spread
    h[m] = min(max((h[a] + h[b]) // 2 + offset, 0), 10)
    fill(h, a, m, spread // 2)
    fill(h, m, b, spread // 2)
h = [0] * 17
h[0] = 7; h[16] = 3
fill(h, 0, 16, 8)
for level in range(10):
    row = 10 - level
    print("".join('#' if v >= row else '.' for v in h))
print(f"heights {h}")
