class Lfu:
    def __init__(self, cap):
        self.cap = cap; self.items = {}; self.tick = 0; self.hits = 0; self.misses = 0
    def get(self, key):
        self.tick += 1
        if key in self.items:
            e = self.items[key]
            e[1] += 1
            e[2] = self.tick
            self.hits += 1
            return e[0]
        self.misses += 1
        return None
    def put(self, key, value):
        self.tick += 1
        if key in self.items:
            e = self.items[key]
            e[0] = value; e[1] += 1; e[2] = self.tick
            return ""
        note = ""
        if len(self.items) == self.cap:
            victim = ""
            best = [0, 1000000, 0]
            for k, e in self.items.items():
                if e[1] < best[1] or (e[1] == best[1] and e[2] < best[2]):
                    victim = k
                    best = e
            del self.items[victim]
            note = f" (evicts {victim}, used {best[1]}x)"
        self.items[key] = [value, 1, self.tick]
        return note

c = Lfu(3)
ops = ["put a 1", "put b 2", "get a", "put c 3", "get a", "get b", "put d 4", "get c", "get d", "put e 5", "get b", "get a"]
for op in ops:
    parts = op.split(" ")
    if parts[0] == "put":
        note = c.put(parts[1], int(parts[2]))
        print(f"{op}{note}")
    else:
        got = c.get(parts[1])
        shown = "miss" if got is None else "hit"
        print(f"{op}: {shown}")
keys = " ".join(sorted(c.items.keys()))
print(f"hits {c.hits}, misses {c.misses}, holding {keys}")
