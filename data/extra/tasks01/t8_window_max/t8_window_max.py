import re
import sys

lines = sys.stdin.read().splitlines()


def invalid():
    print("invalid input")
    sys.exit(0)


if not lines or not re.fullmatch(r"[0-9]+", lines[0].strip()) or int(lines[0].strip()) < 1:
    invalid()
k = int(lines[0].strip())
toks = lines[1].split() if len(lines) > 1 else []
if not all(re.fullmatch(r"-?[0-9]+", t) for t in toks):
    invalid()
xs = [int(t) for t in toks]
if len(xs) < k:
    print("window too large")
    sys.exit(0)
out = [max(xs[i:i + k]) for i in range(len(xs) - k + 1)]
print(" ".join(map(str, out)))
print("overall: %d" % max(out))
