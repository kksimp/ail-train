def parts(v):
    return [int(p) if p.isdigit() else 0 for p in v.split(".")]

def compare(a, b):
    pa = parts(a)
    pb = parts(b)
    for i in range(3):
        if pa[i] != pb[i]:
            return -1 if pa[i] < pb[i] else 1
    return 0

def step(a, b):
    pa = parts(a)
    pb = parts(b)
    return "major" if pa[0] != pb[0] else "minor" if pa[1] != pb[1] else "patch"

old = {"react": "18.2.0", "lodash": "4.17.20", "axios": "0.27.2", "left-pad": "1.3.0", "express": "4.18.2", "chalk": "5.3.0"}
new = {"react": "18.3.1", "lodash": "4.17.21", "axios": "1.6.0", "express": "4.18.2", "chalk": "4.1.2", "zod": "3.22.4"}
counts = {}
for name in sorted(old.keys()):
    before = old[name]
    if name in new:
        after = new[name]
        c = compare(before, after)
        if c < 0:
            kind = step(before, after)
            print(f"upgrade   {name:<9} {before} -> {after} ({kind})")
            counts[kind] = counts.get(kind, 0) + 1
        elif c > 0:
            print(f"DOWNGRADE {name:<9} {before} -> {after}")
            counts["downgrade"] = counts.get("downgrade", 0) + 1
    else:
        print(f"removed   {name:<9} {before}")
        counts["removed"] = counts.get("removed", 0) + 1
for name in sorted(new.keys()):
    if name not in old:
        print(f"added     {name:<9} {new[name]}")
        counts["added"] = counts.get("added", 0) + 1
summary = [f"{v} {k}" for k, v in counts.items()]
print(f"summary: {', '.join(summary)}")
