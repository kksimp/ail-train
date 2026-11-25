import re
import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()

first = lines[0] if lines else ""
if not re.fullmatch(r"-?[0-9]+", first) or int(first) < 1:
    print("bad width")
    sys.exit(0)
width = int(first)

words = []
for line in lines[1:]:
    words.extend(line.split())

rows = []
cur = []
cur_len = 0
for w in words:
    if not cur:
        cur = [w]
        cur_len = len(w)
    elif cur_len + 1 + len(w) > width:
        rows.append(cur)
        cur = [w]
        cur_len = len(w)
    else:
        cur.append(w)
        cur_len += 1 + len(w)
if cur:
    rows.append(cur)


def justify(row):
    if len(row) == 1:
        return row[0]
    gaps = len(row) - 1
    spaces = width - sum(len(w) for w in row)
    if spaces < gaps:
        return " ".join(row)
    base, extra = divmod(spaces, gaps)
    out = ""
    for i, w in enumerate(row):
        out += w
        if i < gaps:
            out += " " * (base + (1 if i < extra else 0))
    return out


for i, row in enumerate(rows):
    if i == len(rows) - 1:
        print(" ".join(row))
    else:
        print(justify(row))
