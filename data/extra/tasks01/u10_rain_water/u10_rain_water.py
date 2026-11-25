import sys
text = sys.stdin.read()
lines = text.split("\n")
if lines and lines[-1] == "":
    lines.pop()
best = None
for l in lines:
    toks = l.split()
    if not all(t.isascii() and t.isdigit() for t in toks):
        print("bad"); continue
    h = [int(t) for t in toks]
    tot = 0
    for i in range(len(h)):
        tot += max(0, min(max(h[:i + 1]), max(h[i:])) - h[i])
    print(tot)
    if best is None or tot > best:
        best = tot
print("max", "none" if best is None else best)
