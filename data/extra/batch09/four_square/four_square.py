def keyed(key):
    seen = set()
    out = []
    for c in key + "ABCDEFGHIJKLMNOPRSTUVWXYZ":
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

def encrypt(msg, k1, k2):
    plain = keyed("")
    top = keyed(k1)
    low = keyed(k2)
    letters = [c for c in msg if c.isalpha() and c != 'Q']
    if len(letters) % 2 == 1:
        letters.append('X')
    out = []
    i = 0
    while i < len(letters):
        a = plain.index(letters[i])
        b = plain.index(letters[i + 1])
        out.append(top[(a // 5) * 5 + b % 5])
        out.append(low[(b // 5) * 5 + a % 5])
        i += 2
    return "".join(out)

def decrypt(code, k1, k2):
    plain = keyed("")
    top = keyed(k1)
    low = keyed(k2)
    out = []
    i = 0
    while i < len(code):
        x = top.index(code[i])
        y = low.index(code[i + 1])
        out.append(plain[(x // 5) * 5 + y % 5])
        out.append(plain[(y // 5) * 5 + x % 5])
        i += 2
    return "".join(out)

k1 = "EXAMPLE"
k2 = "KEYWORD"
top = keyed(k1)
low = keyed(k2)
for r in range(5):
    print("".join(top[r * 5:r * 5 + 5]) + "  " + "".join(low[r * 5:r * 5 + 5]))
for msg in ["HELPMEOBIWANKENOBI", "MEETATNOON", "SECRET"]:
    code = encrypt(msg, k1, k2)
    print(f"{msg:<18} -> {code:<18} -> {decrypt(code, k1, k2)}")
