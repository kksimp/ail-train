def square(key):
    seen = set()
    out = []
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        d = 'I' if c == 'J' else c
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out

def encode(grid, text):
    parts = []
    for c in text:
        if c.isupper():
            d = 'I' if c == 'J' else c
            at = grid.index(d)
            parts.append(f"{at // 5 + 1}{at % 5 + 1}")
    return " ".join(parts)

def decode(grid, code):
    out = []
    for pair in code.split(" "):
        r = int(pair[0])
        c = int(pair[1])
        out.append(grid[(r - 1) * 5 + c - 1])
    return "".join(out)

plain = square("")
for r in range(5):
    print(" ".join(plain[r * 5:r * 5 + 5]))
msg = "ATTACK AT DAWN"
code = encode(plain, msg)
print(f"{msg} -> {code}")
print(f"decoded: {decode(plain, code)}")
keyed = square("ZEBRA")
k = encode(keyed, msg)
print(f"with key ZEBRA: {k} -> {decode(keyed, k)}")
