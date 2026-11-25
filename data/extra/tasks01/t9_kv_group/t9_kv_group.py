import sys

entries = {}
bad = 0
for line in sys.stdin.read().split("\n"):
    if line == "" or line.startswith("#"):
        continue
    if "=" not in line:
        bad += 1
        continue
    k, v = line.split("=", 1)
    k = k.strip(" ")
    v = v.strip(" ")
    if k == "":
        bad += 1
        continue
    if "." in k:
        g, s = k.split(".", 1)
    else:
        g, s = "default", k
    entries[(g, s)] = v
blocks = []
groups = sorted({g for g, _ in entries})
for g in groups:
    lines = ["[" + g + "]"]
    for (gg, s) in sorted(entries):
        if gg == g:
            lines.append(s + " = " + entries[(gg, s)])
    blocks.append("\n".join(lines))
if bad:
    blocks.append("skipped: %d" % bad)
if blocks:
    print("\n\n".join(blocks))
