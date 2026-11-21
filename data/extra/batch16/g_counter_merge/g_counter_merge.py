class GCounter:
    def __init__(s, me, slots):
        s.me, s.slots = me, list(slots)
    def inc(s, n):
        s.slots[s.me] += n
    def merge(s, other):
        for i in range(len(s.slots)):
            s.slots[i] = max(s.slots[i], other.slots[i])
    def value(s):
        return sum(s.slots)

a = GCounter(0, [0, 0, 0])
b = GCounter(1, [0, 0, 0])
c = GCounter(2, [0, 0, 0])
a.inc(3)
b.inc(2)
c.inc(5)
a.inc(1)
print(f"local: a={a.value()} b={b.value()} c={c.value()}")
a.merge(b)
print(f"a merges b: {a.slots} = {a.value()}")
a.merge(b)
print(f"again (idempotent): {a.value()}")
c.merge(a)
b.merge(c)
a.merge(c)
print(f"after gossip: a={a.value()} b={b.value()} c={c.value()}")
x = GCounter(0, [4, 0, 1])
y = GCounter(1, [2, 3, 0])
x2 = GCounter(0, x.slots)
x.merge(y)
y.merge(x2)
print(f"merge order irrelevant: {x.slots} vs {y.slots}")
