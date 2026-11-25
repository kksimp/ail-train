import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()

mode = lines[0] if lines else ""
if mode not in ("exact", "nocase", "trim"):
    print("bad option")
    sys.exit(0)


def key_of(line):
    if mode == "exact":
        return line
    if mode == "nocase":
        return line.lower()
    return line.strip(" \t")


seen = set()
kept = 0
data = lines[1:]
for line in data:
    k = key_of(line)
    if k not in seen:
        seen.add(k)
        print(line)
        kept += 1
print(f"kept {kept} of {len(data)}, dropped {len(data) - kept}")
