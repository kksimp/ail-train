def pr(g, l):
    B = [(100, 85), (250, 135), (500, 210), (1000, 320), (2000, 495), (5000, 790)]; b = next((c for w, c in B if g <= w), -1)
    if b < 0: return "too heavy", 0
    return ("large", b + 450) if l > 60 else ("standard", b)
T = 0
for n, g, l in [("letter", 80, 24), ("book", 640, 30), ("lamp", 1900, 72), ("socks", 230, 20), ("anvil", 9000, 40), ("poster", 300, 90)]:
    k, c = pr(g, l); T += c
    print(f"{n}: {g} g, {k}" if c == 0 else f"{n}: {g} g, {l} cm, {k}, {c // 100}.{c % 100:02}")
print(f"total {T // 100}.{T % 100:02}")
