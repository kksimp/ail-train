class C:
    def __init__(s, n): s.n, s.v, s.o, s.h, s.m = n, {}, [], 0, 0
    def touch(s, k):
        if k in s.o: s.o.remove(k)
        s.o.append(k)
    def get(s, k):
        if k not in s.v: s.m += 1; return -1
        s.h += 1; s.touch(k); return s.v[k]
    def put(s, k, x):
        if k not in s.v and len(s.v) == s.n:
            old = s.o.pop(0); del s.v[old]; print(f"  evict {old}")
        s.v[k] = x; s.touch(k)
c = C(3)
c.put("a", 1); c.put("b", 2); c.put("c", 3)
print(f"get a: {c.get('a')}")
c.put("d", 4)
print(f"get b: {c.get('b')}")
c.put("e", 5)
for k in ["a", "c", "d", "e"]: print(f"get {k}: {c.get(k)}")
print("order [" + ", ".join(f'"{k}"' for k in c.o) + f"], hits {c.h}, misses {c.m}")
