def encode(bs):
    out = []
    i = 0
    while i < len(bs):
        n = min(len(bs) - i, 4)
        v = 0
        for k in range(4):
            b = bs[i + k] if k < n else 0
            v = v * 256 + b
        if v == 0 and n == 4:
            out.append('z')
        else:
            digits = []
            for k in range(5):
                digits.append(chr(v % 85 + 33))
                v = v // 85
            digits.reverse()
            for k in range(n + 1):
                out.append(digits[k])
        i += 4
    return "".join(out)

def decode(text):
    codes = []
    for c in text:
        if c == 'z':
            codes.extend([0] * 5)
        else:
            codes.append(ord(c) - 33)
    out = []
    i = 0
    while i < len(codes):
        n = min(len(codes) - i, 5)
        v = 0
        for k in range(5):
            d = codes[i + k] if k < n else 84
            v = v * 85 + d
        b4 = []
        for k in range(4):
            b4.append(chr(v % 256))
            v = v // 256
        b4.reverse()
        for k in range(n - 1):
            out.append(b4[k])
        i += 5
    return "".join(out)

for s in ["Man ", "Man is", "hello world", "sure.", "AIL"]:
    e = encode([ord(c) for c in s])
    back = decode(e)
    print(f"{s:<12} -> {e:<15} back '{back}'")
print(f"eight zero bytes then 1 -> {encode([0, 0, 0, 0, 0, 0, 0, 0, 1])}")
