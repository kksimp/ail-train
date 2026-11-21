def resolve(fs, path):
    cur = []
    todo = [p for p in path.split("/") if p != ""]
    hops = 0
    while todo:
        comp = todo[0]
        todo = todo[1:]
        if comp == "..":
            if cur:
                cur.pop()
            continue
        if comp == ".":
            continue
        here = "/" + "/".join(cur + [comp])
        if here not in fs:
            return None, f"{here} does not exist"
        kind = fs[here]
        if kind.startswith("link:"):
            hops += 1
            if hops > 8:
                return None, f"too many links at {here}"
            target = kind[5:]
            if target.startswith("/"):
                cur = []
            todo = [p for p in target.split("/") if p != ""] + todo
        elif kind == "file" and todo:
            return None, f"{here} is a file, not a folder"
        else:
            cur.append(comp)
    return f"/{'/'.join(cur)} ({hops} links)", ""

fs = {"/home": "dir", "/home/kai": "dir", "/home/kai/docs": "link:/data/docs", "/data": "dir", "/data/docs": "dir", "/data/docs/plan.txt": "file", "/home/kai/latest": "link:docs/plan.txt", "/home/kai/up": "link:..", "/tmp": "dir", "/tmp/a": "link:/tmp/b", "/tmp/b": "link:a", "/etc": "dir", "/etc/hosts": "file"}
for p in ["/home/kai/docs/plan.txt", "/home/kai/latest", "/home/kai/up/kai/docs", "/tmp/a", "/etc/hosts/x", "/home/bob", "/data/../etc/./hosts"]:
    got, err = resolve(fs, p)
    if got is not None:
        print(f"{p:<24} -> {got}")
    else:
        print(f"{p:<24} !! {err}")
