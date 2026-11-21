class Slab:
    def __init__(s, size, used):
        s.size, s.used = size, used

def class_of(n):
    return 16 if n <= 16 else (32 if n <= 32 else 64)

def alloc(slabs, n):
    c = class_of(n)
    for i in range(len(slabs)):
        if slabs[i].size == c and slabs[i].used != 15:
            slot = 0
            while (slabs[i].used >> slot) & 1 == 1:
                slot += 1
            slabs[i].used = slabs[i].used | (1 << slot)
            return i * 10 + slot
    slabs.append(Slab(c, 1))
    return (len(slabs) - 1) * 10

def picture(used):
    return "".join("#" if (used >> k) & 1 == 1 else "." for k in range(4))

slabs = []
live = {}
requests = [12, 30, 8, 60, 16, 20, 9, 14, 40, -1, 5, -2, 11, 3]
handles = []
for r in requests:
    if r < 0:
        h = handles[0 - r - 1]
        slabs[h // 10].used = slabs[h // 10].used & (15 - (1 << (h % 10)))
        del live[h]
        print(f"free handle {h}")
    else:
        h = alloc(slabs, r)
        handles.append(h)
        live[h] = r
        print(f"{r:>2} bytes -> slab {h // 10} slot {h % 10} ({class_of(r)}-byte class)")
waste = 0
for h, n in live.items():
    waste += slabs[h // 10].size - n
for i, s in enumerate(slabs):
    print(f"slab {i} {s.size:>2} B [{picture(s.used)}]")
print(f"internal waste {waste} bytes over {len(live)} live objects")
