class Extent:
    def __init__(s, logical, physical, count):
        s.logical, s.physical, s.count = logical, physical, count

def append(ex, logical, p):
    if ex:
        last = ex[-1]
        if last.physical + last.count == p and last.logical + last.count == logical:
            last.count += 1
            return
    ex.append(Extent(logical, p, 1))

def build(blocks):
    out = []
    for i, p in enumerate(blocks):
        append(out, i, p)
    return out

def lookup(ex, logical):
    for e in ex:
        if e.logical <= logical < e.logical + e.count:
            return e.physical + logical - e.logical
    return -1

def show(ex):
    for e in ex:
        print(f"    logical {e.logical:>2}..{e.logical + e.count - 1:<2} -> physical {e.physical}..{e.physical + e.count - 1}")

blocks = [100, 101, 102, 103, 200, 201, 57, 58, 59, 60, 61, 300]
ex = build(blocks)
print(f"{len(blocks)} blocks in {len(ex)} extents:")
show(ex)
for l in [0, 5, 9, 11, 12]:
    p = lookup(ex, l)
    spot = "past end of file" if p < 0 else f"physical {p}"
    print(f"block {l:>2} -> {spot}")
n = len(blocks)
append(ex, n, 301)
append(ex, n + 1, 302)
append(ex, n + 2, 400)
print(f"after appending 301, 302, 400: {len(ex)} extents")
show(ex)
