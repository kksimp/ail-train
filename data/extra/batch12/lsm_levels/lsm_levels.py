TOMB = -1

class Lsm:
    def __init__(self):
        self.mem = {}; self.l0 = []; self.l1 = {}
    def put(self, k, v):
        self.mem[k] = v
        if len(self.mem) == 3:
            self.l0.append(self.mem)
            print(f"  flush {len(self.mem)} keys to L0 (now {len(self.l0)} runs)")
            self.mem = {}
        if len(self.l0) == 2:
            merged = dict(self.l1)
            for run in self.l0:
                for key, val in run.items():
                    merged[key] = val
            bottom = {}
            for key in sorted(merged.keys()):
                if merged[key] != TOMB:
                    bottom[key] = merged[key]
            self.l1 = bottom
            self.l0 = []
            print(f"  compact L0 into L1: {len(self.l1)} live keys")
    def get(self, k):
        found = self.mem.get(k)
        where = "memtable"
        if found is None:
            i = len(self.l0) - 1
            while i >= 0 and found is None:
                found = self.l0[i].get(k)
                where = f"L0 run {i}"
                i -= 1
        if found is None:
            found = self.l1.get(k)
            where = "L1"
        if found is None:
            return f"{k}: missing"
        if found == TOMB:
            return f"{k}: deleted ({where})"
        return f"{k}: {found} ({where})"

db = Lsm()
writes = [("cat", 1), ("dog", 2), ("eel", 3), ("cat", 4), ("fox", 5), ("dog", TOMB), ("gnu", 7), ("ant", 8)]
for k, v in writes:
    print(f"put {k} = {v}")
    db.put(k, v)
for k in ["cat", "dog", "eel", "ant"]:
    print(db.get(k))
