def cipher_alphabet(key):
    seen = set()
    out = []
    for c in key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if c.isupper() and c not in seen:
            seen.add(c)
            out.append(c)
    return out

def swap_letters(text, frm, to):
    out = []
    for c in text:
        if c.isupper():
            out.append(to[frm.index(c)])
        else:
            out.append(c)
    return "".join(out)

plain = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for key in ["ZEBRAS", "KANGAROO"]:
    cipher = cipher_alphabet(key)
    print(f"{key:<9} " + "".join(cipher))
cipher = cipher_alphabet("ZEBRAS")
for msg in ["FLEE AT ONCE. WE ARE DISCOVERED!", "THE QUICK BROWN FOX"]:
    code = swap_letters(msg, plain, cipher)
    back = swap_letters(code, cipher, plain)
    print(f"{code} -> {back}")
for key in ["ZEBRAS", "KANGAROO"]:
    other = cipher_alphabet(key)
    fixed = [plain[i] for i in range(26) if plain[i] == other[i]]
    same = "none" if not fixed else "".join(fixed)
    print(f"letters unchanged under {key}: {same}")
