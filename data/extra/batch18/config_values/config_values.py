def render(v):
    k = v[0]
    if k == "n": return str(v[1])
    if k == "t": return f'"{v[1]}"'
    if k == "f": return "yes" if v[1] else "no"
    return "[" + ", ".join(render(x) for x in v[1]) + "]"
def leaves(v): return sum(leaves(x) for x in v[1]) if v[0] == "l" else 1
ports = ("l", [("n", 80), ("n", 443)]); hosts = ("l", [("t", "a.local"), ("t", "b.local")])
st = [("name", ("t", "edge proxy")), ("workers", ("n", 4)), ("tls", ("f", True)), ("ports", ports), ("upstream", ("l", [hosts, ("f", False)]))]
tot = 0
for k, v in st:
    print(f"{k:<9}= {render(v)}"); tot += leaves(v)
print(f"{len(st)} keys, {tot} leaf values")
