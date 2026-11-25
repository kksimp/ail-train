import sys

HEX = "0123456789abcdefABCDEF"


def decode(s):
    out = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c == "+":
            out.append(" ")
            i += 1
        elif c == "%" and i + 3 <= n and s[i + 1] in HEX and s[i + 2] in HEX and int(s[i + 1:i + 3], 16) < 128:
            out.append(chr(int(s[i + 1:i + 3], 16)))
            i += 3
        else:
            out.append(c)
            i += 1
    return "".join(out)


for line in sys.stdin.read().split("\n"):
    u = line.strip(" ")
    if u == "":
        continue
    h = u.find("#")
    if h >= 0:
        u = u[:h]
    q = u.find("?")
    path, query = (u[:q], u[q + 1:]) if q >= 0 else (u, "")
    print("path=" + path)
    for piece in query.split("&"):
        if piece == "":
            continue
        e = piece.find("=")
        k, v = (piece, "") if e < 0 else (piece[:e], piece[e + 1:])
        print("  " + decode(k) + "=" + decode(v))
