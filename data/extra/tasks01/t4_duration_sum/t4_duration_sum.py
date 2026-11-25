import sys
import re

total = valid = invalid = 0
for line in sys.stdin.read().split("\n"):
    t = line.strip(" \t\r")
    if t == "":
        continue
    m = re.fullmatch(r"([0-9]{1,5}):([0-5][0-9]):([0-5][0-9])", t)
    if m is None:
        invalid += 1
        continue
    valid += 1
    total += int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
print(f"total {total // 3600}:{total % 3600 // 60:02d}:{total % 60:02d}")
print(f"valid {valid}")
print(f"invalid {invalid}")
