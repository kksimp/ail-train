import sys

counts = []
k = 0
for line in sys.stdin.read().split("\n"):
    k += 1
    text = line.strip(" ")
    if text == "":
        continue
    s = len(line) - len(line.lstrip(" "))
    level = s // 2
    if s % 2 == 1 or level > len(counts):
        print("error: line %d: bad indent" % k)
        continue
    del counts[level + 1:]
    if len(counts) == level:
        counts.append(0)
    counts[level] += 1
    print(".".join(str(c) for c in counts) + " " + text)
