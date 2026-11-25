## head/tail by line ranges
import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if lines:
    specs = lines[0].split(",")
    data = lines[1:]
    n = len(data)

    def sel(spec, i):
        if spec.startswith("t"):
            return i > n - int(spec[1:])
        if "-" not in spec:
            return i == int(spec)
        a, b = spec.split("-")
        lo = int(a) if a else 1
        hi = int(b) if b else n
        return lo <= i <= hi

    for i in range(1, n + 1):
        if any(sel(s, i) for s in specs):
            print(data[i - 1])
