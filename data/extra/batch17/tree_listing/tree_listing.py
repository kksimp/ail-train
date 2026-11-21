def children(paths, d):
    seen = set()
    for p in paths:
        if p.startswith(d):
            seen.add(p[len(d):].split("/")[0])
    return sorted(seen)

def is_dir(paths, full):
    return any(p.startswith(full + "/") for p in paths)

def draw(paths, d, indent, counts):
    kids = children(paths, d)
    for i, k in enumerate(kids):
        last = i == len(kids) - 1
        joint = "└── " if last else "├── "
        full = d + k
        if is_dir(paths, full):
            counts[0] += 1
            print(f"{indent}{joint}{k}/")
            more = "    " if last else "│   "
            draw(paths, full + "/", indent + more, counts)
        else:
            counts[1] += 1
            print(f"{indent}{joint}{k}")

paths = ["src/main.ail", "src/parse/lexer.ail", "src/parse/tokens.ail", "README.md", "docs/guide.md", "src/util.ail", "tests/lexer_test.ail", "docs/img/logo.png"]
counts = [0, 0]
print(".")
draw(paths, "", "", counts)
print(f"{counts[0]} directories, {counts[1]} files")
