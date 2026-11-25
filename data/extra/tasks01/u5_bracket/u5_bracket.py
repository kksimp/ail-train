import sys
lines = sys.stdin.read().split("\n")
players = [p.strip() for p in lines[0].split(",")]
if len(players) < 2:
    print("error: need 2 players"); sys.exit(0)
seen = set()
for p in players:
    if p in seen:
        print("error: duplicate player " + p); sys.exit(0)
    seen.add(p)
def make(ps):
    ms = []
    for i in range(0, len(ps) - 1, 2):
        ms.append([ps[i], ps[i + 1], ""])
    if len(ps) % 2 == 1:
        ms.append([ps[-1], "", ps[-1]])
    return ms
def fmt(ms):
    out = []
    for a, b, w in ms:
        if b == "":
            out.append("  %s bye" % a)
        else:
            out.append("  %s vs %s -> %s" % (a, b, w if w else "pending"))
    return out
cur = make(players)
done = []
champ = ""
ign = 0
for line in lines[1:]:
    f = line.split()
    if not f:
        continue
    if champ or len(f) != 2:
        ign += 1; continue
    hit = False
    for m in cur:
        if m[2] == "" and ((m[0] == f[0] and m[1] == f[1]) or (m[0] == f[1] and m[1] == f[0])):
            m[2] = f[0]; hit = True; break
    if not hit:
        ign += 1; continue
    if all(m[2] != "" for m in cur):
        done.append(fmt(cur))
        ws = [m[2] for m in cur]
        if len(ws) == 1:
            champ = ws[0]; cur = []
        else:
            cur = make(ws)
for i, r in enumerate(done):
    print("Round %d:" % (i + 1))
    for l in r: print(l)
if cur:
    print("Round %d:" % (len(done) + 1))
    for l in fmt(cur): print(l)
print("Champion: " + (champ if champ else "none yet"))
if ign:
    print("ignored results: %d" % ign)
