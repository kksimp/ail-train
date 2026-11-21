def syndrome(h, r):
    s = 0
    for row in h:
        s = (s << 1) | (bin(r & row).count("1") % 2)
    return s
def weight(x):
    return bin(x).count("1")
def bits(v, n):
    return "".join(str((v >> (n - 1 - i)) & 1) for i in range(n))
h = [52, 42, 25]
leader = [-1] * 8
for e in range(64):
    s = syndrome(h, e)
    if leader[s] < 0 or weight(e) < weight(leader[s]):
        leader[s] = e
for s in range(8):
    print(f"syndrome {bits(s, 3)}: leader {bits(leader[s], 6)} (weight {weight(leader[s])})")
sent = 45
for flip in [0, 4, 32, 12, 9]:
    got = sent ^ flip
    fixed = got ^ leader[syndrome(h, got)]
    verdict = "recovered" if fixed == sent else "wrong"
    print(f"sent {bits(sent, 6)}, received {bits(got, 6)}, decoded {bits(fixed, 6)}: {verdict}")
