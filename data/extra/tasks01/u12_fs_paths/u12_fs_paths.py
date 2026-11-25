import sys


def norm(cwd, p):
    parts = [] if p.startswith("/") else [x for x in cwd.split("/") if x]
    for x in p.split("/"):
        if x == "" or x == ".":
            continue
        if x == "..":
            if parts:
                parts.pop()
        else:
            parts.append(x)
    return "/" + "/".join(parts)


def parent(p):
    i = p.rfind("/")
    return "/" if i == 0 else p[:i]


tree = {"/": "d"}
cwd = "/"
out = []
for raw in sys.stdin.read().splitlines():
    line = raw.strip()
    if not line:
        continue
    w = line.split()
    cmd = w[0]
    if cmd == "pwd" and len(w) == 1:
        out.append(cwd)
    elif cmd == "cd" and len(w) == 2:
        p = norm(cwd, w[1])
        if tree.get(p) == "d":
            cwd = p
        else:
            out.append("cd: no such directory")
    elif cmd in ("mkdir", "touch") and len(w) == 2:
        p = norm(cwd, w[1])
        if p in tree:
            if cmd == "mkdir":
                out.append("mkdir: exists")
            elif tree[p] == "d":
                out.append("touch: is a directory")
        elif tree.get(parent(p)) != "d":
            out.append(f"{cmd}: no such directory")
        else:
            tree[p] = "d" if cmd == "mkdir" else "f"
    elif cmd == "ls" and len(w) <= 2:
        p = norm(cwd, w[1]) if len(w) == 2 else cwd
        if p not in tree:
            out.append("ls: no such file or directory")
        elif tree[p] == "f":
            out.append(p[p.rfind("/") + 1:])
        else:
            names = sorted(k[k.rfind("/") + 1:] + ("/" if tree[k] == "d" else "")
                           for k in tree if k != "/" and parent(k) == p)
            out.append(" ".join(names) if names else "(empty)")
    else:
        out.append("? " + line)
if out:
    print("\n".join(out))
