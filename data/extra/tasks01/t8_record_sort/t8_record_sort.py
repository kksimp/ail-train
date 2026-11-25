import re
import sys

lines = sys.stdin.read().splitlines()


def bad():
    print("bad spec")
    sys.exit(0)


if not lines:
    bad()
keys = []
for part in lines[0].split(","):
    bits = part.split(":")
    if len(bits) != 2 or bits[0] not in ("name", "dept", "salary") or bits[1] not in ("asc", "desc"):
        bad()
    keys.append((bits[0], bits[1] == "desc"))
recs = []
for k, line in enumerate(lines[1:], 2):
    if line == "":
        continue
    f = line.split(",")
    if len(f) != 3 or not f[0] or not f[1] or not re.fullmatch(r"-?[0-9]+", f[2]):
        print("skip %d" % k)
        continue
    recs.append((f[0], f[1], int(f[2])))
idx = {"name": 0, "dept": 1, "salary": 2}
for field, desc in reversed(keys):
    recs.sort(key=lambda r: r[idx[field]], reverse=desc)
for r in recs:
    print("%s,%s,%d" % r)
