def code(c):
    n = ord(c) - 97
    return "".join('B' if ((n >> (4 - k)) & 1) == 1 else 'A' for k in range(5))

def hide(secret, cover):
    ab = "".join(code(c) for c in secret)
    out = []
    used = 0
    for c in cover:
        if c.isalpha() and used < len(ab):
            out.append(c.upper() if ab[used] == 'B' else c)
            used += 1
        else:
            out.append(c)
    return "".join(out)

def reveal(text, want):
    out = []
    n = 0
    count = 0
    for c in text:
        if c.isalpha():
            n = n * 2 + (1 if c.isupper() else 0)
            count += 1
            if count == 5 and len(out) < want:
                out.append(chr(n + 97))
                n = 0
                count = 0
    return "".join(out)

secret = "flee"
groups = " ".join(code(c) for c in secret)
print(f"{secret} -> {groups}")
cover = "the weather is lovely today and the garden looks fine"
hidden = hide(secret, cover)
print(hidden)
print(f"hidden message: {reveal(hidden, 4)}")
marked = sum(1 for c in hidden if c.isupper())
print(f"{marked} capitals carry {len(secret) * 5} symbols")
