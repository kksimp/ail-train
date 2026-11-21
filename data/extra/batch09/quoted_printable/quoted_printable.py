def hex2(n):
    return f"{n:02x}".upper()

def encode_line(cs):
    out = []
    for i, c in enumerate(cs):
        n = ord(c)
        if c == ' ' and i < len(cs) - 1:
            out.append(" ")
        elif 33 <= n <= 126 and c != '=':
            out.append(c)
        else:
            out.append("=" + hex2(n))
    return "".join(out)

def decode_line(cs):
    out = []
    i = 0
    while i < len(cs):
        if cs[i] == '=' and i + 2 < len(cs):
            n = int(cs[i + 1] + cs[i + 2], 16)
            out.append(chr(n))
            i += 3
        else:
            out.append(cs[i])
            i += 1
    return "".join(out)

tab = chr(9)
lines = ["price = 5 euro", "a" + tab + "b", "ends with space ", "100% sure=yes", "plain text"]
same = 0
for line in lines:
    e = encode_line(line)
    if decode_line(e) == line:
        same += 1
    print(e)
print(f"{same} of {len(lines)} lines decode back exactly")
