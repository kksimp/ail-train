import re
import sys

BS = chr(92)
STR = '"[^"' + BS + BS + ']*"'
PAIR = r'\s*' + STR + r'\s*:\s*(?:' + STR + r'|-?\d+|true|false|null)\s*'
OBJ = re.compile(r'\s*\{(' + PAIR + r'(?:,' + PAIR + r')*)?\}\s*')
ITEM = re.compile(r'\s*"([^"' + BS + BS + r']*)"\s*:\s*(?:"([^"' + BS + BS + r']*)"|(-?\d+|true|false|null))\s*')


def q(s):
    return '"' + s + '"' if "," in s else s


cols = []
rows = []
skipped = []
for k, line in enumerate(sys.stdin.read().split("\n"), 1):
    if line == "":
        continue
    m = OBJ.fullmatch(line)
    if not m:
        skipped.append(k)
        continue
    obj = {}
    for im in ITEM.finditer(m.group(1) or ""):
        key = im.group(1)
        if im.group(2) is not None:
            val = im.group(2)
        elif im.group(3) == "null":
            val = ""
        else:
            val = im.group(3)
        obj[key] = val
        if key not in cols:
            cols.append(key)
    rows.append(obj)
if rows:
    print(",".join(q(c) for c in cols))
    for obj in rows:
        print(",".join(q(obj.get(c, "")) for c in cols))
for k in skipped:
    print("skipped line %d" % k)
