class Search:
    def __init__(self, adj):
        n = len(adj)
        self.adj = adj
        self.disc = [0] * n
        self.low = [0] * n
        self.clock = 0
        self.cut = [False] * n

    def visit(self, v, parent):
        self.clock += 1
        self.disc[v] = self.clock
        self.low[v] = self.clock
        children = 0
        for w in self.adj[v]:
            if self.disc[w] == 0:
                children += 1
                self.visit(w, v)
                self.low[v] = min(self.low[v], self.low[w])
                if parent >= 0 and self.low[w] >= self.disc[v]:
                    self.cut[v] = True
            elif w != parent:
                self.low[v] = min(self.low[v], self.disc[w])
        if parent < 0 and children > 1:
            self.cut[v] = True

def build(n, links):
    adj = [[] for _ in range(n)]
    for a, b in links:
        adj[a].append(b)
        adj[b].append(a)
    return adj

names = ["core", "edge1", "edge2", "lab", "dmz", "web", "db", "wifi", "cam"]
links = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6], [3, 7], [7, 8]]
adj = build(len(names), links)
s = Search(adj)
s.visit(0, -1)
count = 0
for v in range(len(names)):
    if s.cut[v]:
        count += 1
        print(f"{names[v]:<6} is a cut point")
print(f"{count} of {len(names)} routers are single points of failure")
