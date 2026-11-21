def leaf(s):
    h = 7
    for c in s:
        h = (h * 131 + ord(c)) % 1000003
    return h

def pair(a, b):
    return (a * 31 + b * 17 + 7) % 1000003

def tree(blocks):
    levels = [[leaf(b) for b in blocks]]
    while len(levels[-1]) > 1:
        below = levels[-1]
        levels.append([pair(below[2 * i], below[2 * i + 1]) for i in range(len(below) // 2)])
    return levels

def diff(a, b, lvl, i, out, checks):
    checks[0] += 1
    if a[lvl][i] == b[lvl][i]:
        return
    if lvl == 0:
        out.append(i)
        return
    diff(a, b, lvl - 1, 2 * i, out, checks)
    diff(a, b, lvl - 1, 2 * i + 1, out, checks)

old = ["intro", "setup", "usage", "config", "faq", "license", "credits", "index"]
new_copy = list(old)
new_copy[2] = "usage v2"
new_copy[6] = "credits!"
ta = tree(old)
tb = tree(new_copy)
top = len(ta) - 1
print(f"root hashes: {ta[top][0]} and {tb[top][0]}")
for lvl in range(len(ta)):
    print(f"level {lvl}: {len(ta[lvl])} hashes")
changed = []
checks = [0]
diff(ta, tb, top, 0, changed, checks)
names = ", ".join(old[i] for i in changed)
print(f"changed blocks {changed}: {names}")
print(f"{checks[0]} hash comparisons instead of {len(old)}")
