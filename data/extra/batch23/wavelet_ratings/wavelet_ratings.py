class WNode:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.counts = [0]
        self.left = -1
        self.right = -1

def build(nodes, xs, lo, hi):
    idx = len(nodes)
    nodes.append(WNode(lo, hi))
    if lo == hi or len(xs) == 0:
        return idx
    mid = (lo + hi) // 2
    counts = [0]
    ls = []
    rs = []
    for x in xs:
        if x <= mid:
            ls.append(x)
            counts.append(counts[-1] + 1)
        else:
            rs.append(x)
            counts.append(counts[-1])
    l = build(nodes, ls, lo, mid)
    r = build(nodes, rs, mid + 1, hi)
    nodes[idx].counts = counts
    nodes[idx].left = l
    nodes[idx].right = r
    return idx

def kth(nodes, at, l, r, k):
    n = nodes[at]
    if n.lo == n.hi:
        return n.lo
    went_left = n.counts[r] - n.counts[l]
    if k <= went_left:
        return kth(nodes, n.left, n.counts[l], n.counts[r], k)
    return kth(nodes, n.right, l - n.counts[l], r - n.counts[r], k - went_left)

stars = [3, 7, 1, 4, 4, 6, 2, 7, 5, 0, 3, 6, 7, 2, 4, 5]
nodes = []
root = build(nodes, stars, 0, 7)
print(f"ratings: {stars} ({len(nodes)} tree nodes)")
for q in [[0, 16], [3, 9], [8, 14]]:
    size = q[1] - q[0]
    k = (size + 1) // 2
    part = sorted(stars[q[0]:q[1]])
    print(f"median of days {q[0]}..{q[1] - 1}: {kth(nodes, root, q[0], q[1], k)} (check {part[k - 1]})")
