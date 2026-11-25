import re
import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()

m = re.fullmatch(r"(enc|dec) (-?[0-9]+)", lines[0]) if lines else None
if not m:
    print("bad key")
    sys.exit(0)
k = int(m.group(2))
if m.group(1) == "dec":
    k = -k
k %= 26


def shift(c):
    if "A" <= c <= "Z":
        return chr(65 + (ord(c) - 65 + k) % 26)
    if "a" <= c <= "z":
        return chr(97 + (ord(c) - 97 + k) % 26)
    return c


for line in lines[1:]:
    print("".join(shift(c) for c in line))
