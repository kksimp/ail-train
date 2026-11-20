def vig(t, key, d):
    ks = [ord(c) - 97 for c in key.lower()]
    out, i = [], 0
    for c in t:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            out.append(chr((ord(c) - base + d * ks[i % len(ks)] + 26) % 26 + base))
            i += 1
        else:
            out.append(c)
    return "".join(out)
plain = "Attack at dawn, then Rest."
for key in ["lemon", "b", "Key"]:
    e = vig(plain, key, 1)
    print(f"{key}: {e} | back: {str(vig(e, key, -1) == plain).lower()}")
print(vig("abc xyz", "a", 1))
