def affected(imports, edited):
    users = {}
    for m, deps in imports.items():
        for d in deps:
            users.setdefault(d, []).append(m)
    why = {}
    queue = []
    for e in edited:
        why[e] = "edited"
        queue.append(e)
    head = 0
    while head < len(queue):
        cur = queue[head]
        head += 1
        for u in users.get(cur, []):
            if u not in why:
                why[u] = f"imports {cur}"
                queue.append(u)
    return why

imports = {"app": ["http", "config", "views"], "http": ["net", "strings"], "views": ["html", "strings"], "html": ["strings"], "config": ["json"], "json": ["strings"], "net": [], "strings": [], "cli": ["config"]}
for edited in [["html"], ["json"], ["strings"]]:
    why = affected(imports, edited)
    print(f"edit {edited[0]}: {len(why)} of {len(imports)} modules rebuild")
    for m in sorted(why):
        print(f"    {m:<8} {why[m]}")
