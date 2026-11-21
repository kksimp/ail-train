def inv_mod(a):
    for k in range(1, 26):
        if (a * k) % 26 == 1:
            return k
    return 0

def md(x):
    return (x % 26 + 26) % 26

def apply(m, text):
    cs = list(text)
    if len(cs) % 2 == 1:
        cs.append('X')
    out = []
    i = 0
    while i < len(cs):
        a = ord(cs[i]) - 65
        b = ord(cs[i + 1]) - 65
        out.append(chr(md(m[0][0] * a + m[0][1] * b) + 65))
        out.append(chr(md(m[1][0] * a + m[1][1] * b) + 65))
        i += 2
    return "".join(out)

def inverse(m):
    det = md(m[0][0] * m[1][1] - m[0][1] * m[1][0])
    d = inv_mod(det)
    return [[md(d * m[1][1]), md(-d * m[0][1])], [md(-d * m[1][0]), md(d * m[0][0])]]

key = [[3, 3], [2, 5]]
inv = inverse(key)
det = md(3 * 5 - 3 * 2)
print(f"key {key}, determinant {det}, inverse {inv}")
for msg in ["HELP", "SHORTEXAMPLE", "ATTACKATDAWN", "ODD"]:
    code = apply(key, msg)
    print(f"{msg:<13} -> {code:<13} -> {apply(inv, code)}")
bad = [[2, 4], [6, 8]]
bd = md(2 * 8 - 4 * 6)
print(f"key {bad} has determinant {bd}, inverse mod 26 {inv_mod(bd)}: unusable")
