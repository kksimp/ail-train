class Trie:
    def __init__(self):
        self.kids = [{}]
        self.ends = [False]

    def add(self, w):
        at = 0
        for c in w:
            if c not in self.kids[at]:
                self.kids.append({})
                self.ends.append(False)
                self.kids[at][c] = len(self.kids) - 1
            at = self.kids[at][c]
        self.ends[at] = True

def show(t, at, depth, lines):
    for c in sorted(t.kids[at].keys()):
        label = [c]
        node = t.kids[at][c]
        while len(t.kids[node]) == 1 and not t.ends[node]:
            only = sorted(t.kids[node].keys())[0]
            label.append(only)
            node = t.kids[node][only]
        pad = " " * (depth * 2)
        mark = " *" if t.ends[node] else ""
        piece = "".join(label)
        lines.append(f"{pad}{piece}{mark}")
        show(t, node, depth + 1, lines)

words = ["romane", "romanus", "romulus", "rubens", "ruber", "rubicon", "rubicundus", "rub"]
t = Trie()
for w in words:
    t.add(w)
lines = []
show(t, 0, 0, lines)
print(f"trie nodes {len(t.kids)}, radix nodes {len(lines) + 1} (with the root)")
for l in lines:
    print(l)
