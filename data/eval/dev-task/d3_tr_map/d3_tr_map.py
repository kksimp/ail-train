## tr-style character mapping
import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if lines:
    s1, s2 = lines[0].split(" ")
    table = {}
    for i, ch in enumerate(s1):
        if ch not in table:
            table[ch] = s2[i] if i < len(s2) else s2[-1]
    for line in lines[1:]:
        print("".join(table.get(c, c) for c in line))
