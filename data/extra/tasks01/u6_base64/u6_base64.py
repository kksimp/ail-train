import sys

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode(text):
    data = [ord(c) for c in text]
    out = []
    for i in range(0, len(data), 3):
        chunk = data[i:i + 3]
        n = 0
        for k in range(3):
            n = (n << 8) | (chunk[k] if k < len(chunk) else 0)
        out.append(ALPHA[(n >> 18) & 63])
        out.append(ALPHA[(n >> 12) & 63])
        out.append(ALPHA[(n >> 6) & 63] if len(chunk) > 1 else "=")
        out.append(ALPHA[n & 63] if len(chunk) > 2 else "=")
    return "".join(out)


def decode(text):
    if len(text) % 4 != 0:
        return None
    vals = []
    pad = 0
    for c in text:
        if c == "=":
            pad += 1
            vals.append(0)
        else:
            if pad > 0 or c not in ALPHA:
                return None
            vals.append(ALPHA.index(c))
    if pad > 2:
        return None
    out = []
    for i in range(0, len(vals), 4):
        n = (vals[i] << 18) | (vals[i + 1] << 12) | (vals[i + 2] << 6) | vals[i + 3]
        count = 3 - pad if i + 4 == len(vals) else 3
        for k in range(count):
            b = (n >> (16 - 8 * k)) & 255
            if b < 32 or b > 126:
                return None
            out.append(chr(b))
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
