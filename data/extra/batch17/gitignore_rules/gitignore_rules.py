def glob(p, i, s, j):
    if i == len(p):
        return j == len(s)
    if p[i] == '*':
        k = j
        while True:
            if glob(p, i + 1, s, k):
                return True
            if k == len(s) or s[k] == '/':
                return False
            k += 1
    if j < len(s) and (p[i] == '?' or p[i] == s[j]) and s[j] != '/':
        return glob(p, i + 1, s, j + 1)
    if j < len(s) and p[i] == '/' and s[j] == '/':
        return glob(p, i + 1, s, j + 1)
    return False

def decide(path, is_dir, pats):
    base = path.split("/")[-1]
    hit = ""
    for raw in pats:
        neg = raw.startswith("!")
        pat = raw[1:] if neg else raw
        dir_only = pat.endswith("/")
        if dir_only:
            pat = pat[:-1]
        if dir_only and not is_dir:
            continue
        anchored = "/" in pat
        if anchored and pat.startswith("/"):
            pat = pat[1:]
        target = path if anchored else base
        if glob(list(pat), 0, list(target), 0):
            hit = "" if neg else raw
    return hit

def why_ignored(path, pats):
    parts = path.split("/")
    for k in range(1, len(parts)):
        dir_hit = decide("/".join(parts[:k]), True, pats)
        if dir_hit != "":
            return dir_hit
    return decide(path, False, pats)

pats = ["*.log", "!keep.log", "build/", "/todo.txt", "docs/*.pdf", "temp*"]
paths = ["app.log", "logs/keep.log", "logs/err.log", "build/out/app.js", "src/build.rs", "todo.txt", "src/todo.txt", "docs/guide.pdf", "docs/api/ref.pdf", "temp_notes.md", "src/tempfile.c"]
kept = 0
for p in paths:
    hit = why_ignored(p, pats)
    if hit == "":
        kept += 1
        print(f"{p:<18} kept")
    else:
        print(f"{p:<18} ignored by {hit}")
print(f"{kept} of {len(paths)} files kept")
