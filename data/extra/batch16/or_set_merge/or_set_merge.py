class OrSet:
    def __init__(s, name):
        s.name, s.count, s.adds, s.tombs = name, 0, {}, set()
    def add(s, item):
        s.count += 1
        s.adds[f"{s.name}{s.count}"] = item
    def remove(s, item):
        for tag, it in s.adds.items():
            if it == item:
                s.tombs.add(tag)
    def merge(s, o):
        for tag, it in o.adds.items():
            s.adds[tag] = it
        s.tombs |= o.tombs
    def items(s):
        return sorted(set(it for tag, it in s.adds.items() if tag not in s.tombs))

def show(xs):
    return "[" + ", ".join(xs) + "]"

a = OrSet("A")
b = OrSet("B")
a.add("milk")
a.add("eggs")
b.merge(a)
print(f"synced: A {show(a.items())} B {show(b.items())}")
b.remove("milk")
a.add("milk")
b.add("bread")
a.remove("eggs")
print(f"apart:  A {show(a.items())} B {show(b.items())}")
a.merge(b)
b.merge(a)
print(f"merged: A {show(a.items())} B {show(b.items())}")
print(f"tags {len(a.adds)}, tombstones {len(a.tombs)}")
