import re
import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()

mode = lines[0] if lines else ""
if mode not in ("encode", "decode"):
    print("bad mode")
    sys.exit(0)


def encode(line):
    if any(c in "0123456789" for c in line):
        return None
    out = []
    i = 0
    while i < len(line):
        j = i
        while j < len(line) and line[j] == line[i]:
            j += 1
        out.append(f"{j - i}{line[i]}")
        i = j
    return "".join(out)


def decode(line):
    if not re.fullmatch(r"(?:[1-9][0-9]*[^0-9])*", line):
        return None
    return "".join(ch * int(n) for n, ch in re.findall(r"([1-9][0-9]*)([^0-9])", line))


for line in lines[1:]:
    res = encode(line) if mode == "encode" else decode(line)
    print("error" if res is None else res)
