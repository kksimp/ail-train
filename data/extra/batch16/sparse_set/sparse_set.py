class SparseSet:
    def __init__(s, cap):
        s.dense, s.sparse = [], [0] * cap
    def has(s, x):
        i = s.sparse[x]
        return i < len(s.dense) and s.dense[i] == x
    def add(s, x):
        if not s.has(x):
            s.sparse[x] = len(s.dense)
            s.dense.append(x)
    def remove(s, x):
        if s.has(x):
            i = s.sparse[x]
            last = s.dense[-1]
            s.dense[i] = last
            s.sparse[last] = i
            s.dense.pop()

def b(v):
    return "true" if v else "false"

s = SparseSet(16)
for x in [5, 9, 2, 14, 9, 7]:
    s.add(x)
print(f"after adds    dense {s.dense}")
s.remove(9)
print(f"remove 9      dense {s.dense}")
s.remove(3)
s.remove(5)
print(f"remove 3, 5   dense {s.dense}")
print(f"has 14 {b(s.has(14))}, has 9 {b(s.has(9))}, has 5 {b(s.has(5))}")
print(f"sparse table  {s.sparse}")
s.dense = []
print(f"cleared: has 2 {b(s.has(2))} though sparse[2] holds {s.sparse[2]}")
s.add(2)
print(f"add 2 again   dense {s.dense}")
