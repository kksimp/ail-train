def mix(h, x):
    return (h * 31 + x) % 2147483647

def text_hash(s):
    h = 17
    for c in s:
        h = mix(h, ord(c))
    return h

def build(label, src, steps, cache):
    out = {}
    report = []
    for st in steps:
        key = text_hash(st[0])
        for inp in st[1:]:
            key = mix(key, src[inp] if inp in src else out.get(inp, 0))
        if key in cache:
            report.append(f"{st[0]} hit")
        else:
            cache[key] = mix(key, 7)
            report.append(f"{st[0]} MISS")
        out[st[0]] = cache[key]
    print(f"{label}: {', '.join(report)}")

steps = [["cc_a", "a.c"], ["cc_b", "b.c", "common.h"], ["cc_c", "c.c", "common.h"], ["link", "cc_a", "cc_b", "cc_c"], ["test", "link", "cases.txt"], ["docs", "guide.md"]]
src = {"a.c": 101, "b.c": 202, "c.c": 303, "common.h": 404, "cases.txt": 505, "guide.md": 606}
cache = {}
build("clean build", src, steps, cache)
build("no change  ", src, steps, cache)
src["b.c"] = 222
build("edit b.c   ", src, steps, cache)
src["b.c"] = 202
build("undo edit  ", src, steps, cache)
src["common.h"] = 444
build("edit header", src, steps, cache)
print(f"cache holds {len(cache)} entries")
