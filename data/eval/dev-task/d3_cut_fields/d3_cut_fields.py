## cut by delimiter and field list
import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if lines:
    opt = lines[0]
    delim = opt[2]
    spec = opt[6:]
    fields = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            fields.extend(range(int(a), int(b) + 1))
        else:
            fields.append(int(part))
    for line in lines[1:]:
        if delim not in line:
            print(line)
            continue
        cols = line.split(delim)
        out = [cols[f - 1] if f <= len(cols) else "" for f in fields]
        print(delim.join(out))
