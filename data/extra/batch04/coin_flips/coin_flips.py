s = 2024; h = 0
for b in range(1, 5):
    f = ""; L = 0; r = 0; p = "x"
    for _ in range(50):
        s = (s * 1103515245 + 12345) % 2147483648; c = "H" if (s // 65536) % 2 == 0 else "T"
        if c == "H": h += 1
        r = r + 1 if c == p else 1; L = max(L, r); p = c; f += c
    print(f"block {b}: {f[:20]}... longest run {L}")
print(f"heads: {h} of 200 ({h / 200:.3f})")
