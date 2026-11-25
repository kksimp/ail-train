## uniq with options
import sys
from itertools import groupby

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if lines:
    opt = lines[0]
    keyf = (lambda s: s.lower()) if "i" in opt else (lambda s: s)
    for _, grp in groupby(lines[1:], key=keyf):
        grp = list(grp)
        n = len(grp)
        if "d" in opt and n < 2:
            continue
        if "u" in opt and n != 1:
            continue
        if "c" in opt:
            print("%4d %s" % (n, grp[0]))
        else:
            print(grp[0])
