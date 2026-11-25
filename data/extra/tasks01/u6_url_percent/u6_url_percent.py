import sys

SAFE = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~")
HEX = "0123456789abcdefABCDEF"


def encode(text):
    out = []
    for c in text:
        if c in SAFE:
            out.append(c)
        else:
            out.append("%%%02X" % ord(c))
    return "".join(out)


def decode(text):
    out = []
    i = 0
    while i < len(text):
        c = text[i]
        if c == "%":
            if i + 2 >= len(text):
                return None
            h = text[i + 1:i + 3]
            if len(h) < 2 or h[0] not in HEX or h[1] not in HEX:
                return None
            code = int(h, 16)
            if code < 32 or code > 126:
                return None
            out.append(chr(code))
            i += 3
        elif c == "+":
            out.append(" ")
            i += 1
        else:
            out.append(c)
            i += 1
    return "".join(out)


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        parts = line.split(" ", 1)
        arg = parts[1] if len(parts) > 1 else ""
        if parts[0] == "enc":
            print(encode(arg))
        elif parts[0] == "dec":
            r = decode(arg)
            print("invalid" if r is None else r)
        else:
            print("bad command")


main()
