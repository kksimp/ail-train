def ext(name):
    dot = name.rfind(".")
    return "(none)" if dot < 0 else name[dot + 1:]

def group(xs, key):
    out = {}
    for x in xs:
        out.setdefault(key(x), []).append(x)
    return out

def show(groups):
    for k in sorted(groups):
        print(f"{k}: {' '.join(groups[k])} ({len(groups[k])})")

show(group(["a.ail", "notes.txt", "b.ail", "Makefile", "c.txt", "d.ail"], ext))
show(group(["ann", "bob", "alice", "cy", "bea"], lambda p: p[:1]))
sizes = group([3, 14, 7, 20, 1], lambda n: n >= 10)
print(",".join(map(str, sizes.get(False, []))) + " | " + ",".join(map(str, sizes.get(True, []))))
