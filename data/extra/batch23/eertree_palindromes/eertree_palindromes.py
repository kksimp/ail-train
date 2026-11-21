class Eertree:
    def __init__(self):
        self.lens = [-1, 0]
        self.links = [0, 0]
        self.edges = [{}, {}]
        self.text = []
        self.last = 1

    def fits(self, u, i):
        l = self.lens[u]
        return i - l - 1 >= 0 and self.text[i - l - 1] == self.text[i]

    def suffix_for(self, v, i):
        u = v
        while not self.fits(u, i):
            u = self.links[u]
        return u

    def add(self, c):
        self.text.append(c)
        i = len(self.text) - 1
        cur = self.suffix_for(self.last, i)
        if c in self.edges[cur]:
            self.last = self.edges[cur][c]
            return False
        node = len(self.lens)
        self.lens.append(self.lens[cur] + 2)
        self.edges.append({})
        if self.lens[node] == 1:
            self.links.append(1)
        else:
            w = self.suffix_for(self.links[cur], i)
            self.links.append(self.edges[w][c])
        self.edges[cur][c] = node
        self.last = node
        return True

def palindromes(s):
    t = Eertree()
    found = []
    for i in range(len(s)):
        if t.add(s[i]):
            l = t.lens[t.last]
            found.append(s[i - l + 1:i + 1])
    return found

for s in ["abacaba", "banana", "aaaa", "racecars", "abcd"]:
    ps = palindromes(s)
    shown = " ".join(ps)
    print(f"{s:<9} {len(ps)} distinct: {shown}")
