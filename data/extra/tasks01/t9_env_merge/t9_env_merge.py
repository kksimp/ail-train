import re
import sys

KEY = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if "---" in lines:
    p = lines.index("---")
    base, over = lines[:p], lines[p + 1:]
else:
    base, over = lines, []
env = {}
bad = 0
for block, is_over in ((base, False), (over, True)):
    for line in block:
        if line.strip() == "" or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:]
        if "=" in line:
            k, v = line.split("=", 1)
            k = k.strip()
            if KEY.fullmatch(k):
                env[k] = v.strip()
            else:
                bad += 1
        elif is_over and line.startswith("-") and KEY.fullmatch(line[1:].strip()):
            env.pop(line[1:].strip(), None)
        else:
            bad += 1
for k, v in env.items():
    print("%s=%s" % (k, v))
if bad:
    print("# skipped %d" % bad)
