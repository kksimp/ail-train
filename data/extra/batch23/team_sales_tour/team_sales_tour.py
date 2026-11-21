class Fenwick:
    def __init__(self, size):
        self.tree = [0] * size

    def add(self, i, delta):
        k = i + 1
        while k < len(self.tree):
            self.tree[k] += delta
            k += k & (-k)

    def prefix(self, i):
        k = i
        s = 0
        while k > 0:
            s += self.tree[k]
            k -= k & (-k)
        return s

def tour(kids, v, tin, tout, clock):
    tin[v] = clock[0]
    clock[0] += 1
    for c in kids[v]:
        tour(kids, c, tin, tout, clock)
    tout[v] = clock[0]

def report(names, managers, fw, tin, tout):
    for m in managers:
        total = fw.prefix(tout[m]) - fw.prefix(tin[m])
        print(f"  team of {names[m]:<5} {total:>4} (people {tin[m]}..{tout[m] - 1} in tour order)")

names = ["Ana", "Ben", "Cleo", "Dev", "Eve", "Finn", "Gia", "Hal"]
parent = [-1, 0, 0, 1, 1, 2, 2, 5]
sales = [10, 40, 25, 70, 55, 30, 45, 60]
kids = [[] for _ in names]
tin = [0] * len(names)
tout = [0] * len(names)
for v in range(1, len(names)):
    kids[parent[v]].append(v)
clock = [0]
tour(kids, 0, tin, tout, clock)
fw = Fenwick(9)
for v in range(len(names)):
    fw.add(tin[v], sales[v])
managers = [0, 1, 2, 5]
print("monthly sales by team:")
report(names, managers, fw, tin, tout)
fw.add(tin[7], 25)
fw.add(tin[3], -20)
print("after Hal sells 25 more and Dev returns 20:")
report(names, managers, fw, tin, tout)
