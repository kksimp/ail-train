nodes = [[{}, False]]
def ins(w):
    at = 0
    for c in w:
        if c in nodes[at][0]: at = nodes[at][0][c]
        else:
            nodes.append([{}, False]); nodes[at][0][c] = len(nodes) - 1; at = len(nodes) - 1
    nodes[at][1] = True
def find(t):
    at = 0
    for c in t:
        if c not in nodes[at][0]: return None
        at = nodes[at][0][c]
    return at
def col(at, p, out):
    if nodes[at][1]: out.append(p)
    for c in sorted(nodes[at][0]): col(nodes[at][0][c], p + c, out)
for w in ["car", "cart", "care", "cat", "dog", "dot", "do", "card"]: ins(w)
print(f"nodes: {len(nodes)}")
for p in ["car", "do", "ca", "x"]:
    out = []
    at = find(p)
    if at is not None: col(at, p, out)
    wh = "word" if p in out else "prefix only"
    print(f"{p}: {len(out)} words [" + ", ".join(f'"{w}"' for w in out) + f"] ({wh})")
