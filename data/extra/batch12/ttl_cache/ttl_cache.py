def source(key):
    return sum(ord(c) for c in key) * 3

class TtlCache:
    def __init__(self, ttl):
        self.ttl = ttl; self.items = {}; self.fetches = 0
    def read(self, key, now):
        if key in self.items:
            v, exp = self.items[key]
            if now < exp:
                return f"hit {v}"
        self.fetches += 1
        v = source(key)
        self.items[key] = (v, now + self.ttl)
        return f"miss, fetched {v}"
    def sweep(self, now):
        old = [k for k in self.items if self.items[k][1] <= now]
        for k in old:
            del self.items[k]
        return len(old)

c = TtlCache(10)
reads = [(1, "tea"), (3, "rice"), (8, "tea"), (12, "salt"), (16, "tea"), (19, "rice"), (22, "tea"), (27, "salt"), (33, "oil")]
next_sweep = 10
for now, key in reads:
    while next_sweep <= now:
        gone = c.sweep(next_sweep)
        print(f"  sweep at {next_sweep}s dropped {gone}")
        next_sweep += 10
    print(f"t={now:>2}s {key:<5} {c.read(key, now)}")
print(f"{c.fetches} fetches for {len(reads)} reads")
