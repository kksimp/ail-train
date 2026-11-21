def ioc(cs):
    counts = {}
    for c in cs:
        counts[c] = counts.get(c, 0) + 1
    n = len(cs)
    total = 0
    for c, k in counts.items():
        total += k * (k - 1)
    return total / (n * (n - 1))

def vigenere(text, key):
    out = []
    for i, c in enumerate(text):
        v = (ord(c) - 65 + ord(key[i % len(key)]) - 65) % 26
        out.append(chr(v + 65))
    return out

plain = list("ITWASTHEBESTOFTIMESITWASTHEWORSTOFTIMESITWASTHEAGEOFWISDOMITWASTHEAGEOFFOOLISHNESSITWASTHEEPOCHOFBELIEFITWASTHEEPOCHOFINCREDULITYITWASTHESEASONOFLIGHT")
code = vigenere(plain, "LEMON")
print(f"plain text ioc {ioc(plain):.4f}, cipher text ioc {ioc(code):.4f}")
best = 0
best_score = 0.0
for period in range(1, 9):
    score = 0.0
    for start in range(period):
        column = []
        i = start
        while i < len(code):
            column.append(code[i])
            i += period
        score += ioc(column)
    avg = score / period
    print(f"key length {period}: average column ioc {avg:.4f}")
    if avg > best_score:
        best_score = avg
        best = period
print(f"most likely key length: {best}")
