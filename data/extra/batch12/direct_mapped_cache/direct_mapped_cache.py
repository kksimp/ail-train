def split(addr, sets):
    block = addr // 16
    return [block // sets, block % sets, addr % 16]

def simulate(addrs, ways):
    sets = 4 // ways
    tags = [[] for _ in range(sets)]
    hits = 0
    for a in addrs:
        tag, st, off = split(a, sets)
        if tag in tags[st]:
            hits += 1
            tags[st].remove(tag)
        elif len(tags[st]) == ways:
            tags[st].pop(0)
        tags[st].append(tag)
    return hits

addrs = [0, 4, 64, 8, 68, 128, 0, 72, 132, 16, 80, 20, 0, 64]
for a in addrs[0:5]:
    p = split(a, 4)
    print(f"address {a:>3}: tag {p[0]}, set {p[1]}, offset {p[2]:>2}")
d = simulate(addrs, 1)
s = simulate(addrs, 2)
f = simulate(addrs, 4)
print(f"direct-mapped: {d} of {len(addrs)} hits")
print(f"2-way:         {s} of {len(addrs)} hits")
print(f"fully assoc.:  {f} of {len(addrs)} hits")
