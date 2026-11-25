import sys

for raw in sys.stdin.read().split("\n"):
    t = raw.strip()
    if t == "":
        continue
    if len(t) > 18 or not all(c in "0123456789" for c in t):
        print(t + ": invalid")
        continue
    n = int(t)
    chain = [n]
    while chain[-1] >= 10:
        chain.append(sum(int(c) for c in str(chain[-1])))
    print("%d: %s steps=%d" % (n, " -> ".join(str(x) for x in chain), len(chain) - 1))
