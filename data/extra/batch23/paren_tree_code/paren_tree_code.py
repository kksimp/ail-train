def encode(kids, v, out):
    out.append('(')
    for c in kids[v]:
        encode(kids, c, out)
    out.append(')')

def find_close(bp, i):
    depth = 0
    j = i
    while j < len(bp):
        depth += 1 if bp[j] == '(' else -1
        if depth == 0:
            return j
        j += 1
    return -1

def enclose(bp, i):
    depth = 0
    j = i - 1
    while j >= 0:
        depth += 1 if bp[j] == ')' else -1
        if depth < 0:
            return j
        j -= 1
    return -1

names = ["root", "docs", "src", "a.md", "b.md", "lib", "main", "x.rs", "y.rs", "test"]
parent = [-1, 0, 0, 1, 1, 2, 2, 5, 5, 0]
kids = [[] for _ in names]
for v in range(1, len(names)):
    kids[parent[v]].append(v)
bp = []
encode(kids, 0, bp)
shown = "".join(bp)
print(f"{shown} ({len(bp)} bits for {len(names)} nodes)")
opens = [i for i in range(len(bp)) if bp[i] == '(']
order = []
stack = [0]
while stack:
    v = stack.pop()
    order.append(v)
    k = len(kids[v]) - 1
    while k >= 0:
        stack.append(kids[v][k])
        k -= 1
for n in range(len(names)):
    i = opens[n]
    depth = bp[0:i].count('(') - bp[0:i].count(')')
    size = (find_close(bp, i) - i + 1) // 2
    up = enclose(bp, i)
    boss = "-" if up < 0 else names[order[opens.index(up)]]
    print(f"{names[order[n]]:<5} depth {depth} subtree {size:>2} parent {boss}")
