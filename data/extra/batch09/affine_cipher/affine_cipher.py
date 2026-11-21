def inverse(a):
    for k in range(1, 26):
        if (a * k) % 26 == 1:
            return k, None
    return None, f"a = {a} has no inverse mod 26"

def shift_text(text, mul, add):
    out = []
    for c in text:
        if c.isupper():
            x = ord(c) - 65
            y = ((mul * x + add) % 26 + 26) % 26
            out.append(chr(y + 65))
        else:
            out.append(c)
    return "".join(out)

msg = "MEET ME AT THE OLD MILL"
for a, b in [(5, 8), (7, 3), (25, 0), (13, 1)]:
    inv, err = inverse(a)
    if inv is not None:
        secret = shift_text(msg, a, b)
        back = shift_text(secret, inv, -inv * b)
        print(f"a={a:<2} b={b} inverse {inv:<2} {secret} -> {back}")
    else:
        print(f"a={a:<2} b={b} refused: {err}")
