import sys

lines = [l.strip() for l in sys.stdin.read().splitlines()]
if "---" not in lines:
    print("error: missing separator")
    sys.exit(0)
sep = lines.index("---")
table = {}
for l in lines[:sep]:
    if len(l) == 5 and l[3] == "=" and set(l[:3]) <= set("ACGT"):
        a = l[4]
        if "A" <= a <= "Z" or a == "*":
            table[l[:3]] = a
k = 0
for s in lines[sep + 1:]:
    if not s:
        continue
    k += 1
    if not set(s) <= set("ACGT"):
        print(f"{k} invalid")
        continue
    i = s.find("ATG")
    if i < 0:
        print(f"{k} no start")
        continue
    prot = ""
    end = "open"
    while i + 3 <= len(s):
        c = s[i:i + 3]
        if c not in table:
            end = "unknown:" + c
            break
        if table[c] == "*":
            end = "stop"
            break
        prot += table[c]
        i += 3
    print(f"{k} protein={prot} len={len(prot)} end={end}")
