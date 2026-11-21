text = ["1,0,1~1,2,1", "0,0,2~2,0,2", "0,2,3~2,2,3", "0,0,4~0,2,4", "2,0,5~2,2,5", "0,1,6~2,1,6", "1,1,8~1,1,9", "0,0,11~0,0,11"]
slabs = []
for t in text:
    a, b = [[int(v) for v in e.split(",")] for e in t.split("~")]
    cells = [x * 10 + y for x in range(a[0], b[0] + 1) for y in range(a[1], b[1] + 1)]
    slabs.append((cells, a[2], b[2]))
slabs.sort(key=lambda s: s[1])
top = {}; owner = {}; sup = []
for i, (cells, z1, z2) in enumerate(slabs):
    floor = max(top.get(c, 0) for c in cells)
    below = set()
    for c in cells:
        if floor > 0 and top.get(c, 0) == floor:
            below.add(owner[c])
    for c in cells:
        top[c] = floor + 1 + (z2 - z1); owner[c] = i
    sup.append(below)

def falls(sup, removed):
    gone = {removed}
    for i in range(removed + 1, len(sup)):
        if sup[i] and sup[i] <= gone:
            gone.add(i)
    return len(gone) - 1

for i, s in enumerate(sup):
    print(f"slab {i} rests on {len(s)} slab(s)")
print(f"part 1: {sum(1 for i in range(len(sup)) if falls(sup, i) == 0)} slabs can be removed safely")
print(f"part 2: {sum(falls(sup, i) for i in range(len(sup)))} slabs fall in total")
