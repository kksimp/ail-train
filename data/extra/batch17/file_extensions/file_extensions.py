def split_ext(name):
    doubles = [".tar.gz", ".tar.bz2", ".tar.xz"]
    low = name.lower()
    for d in doubles:
        if low.endswith(d) and len(low) > len(d):
            cut = len(name) - len(d)
            return [name[:cut], d[1:]]
    dot = name.rfind(".")
    if dot <= 0 or dot == len(name) - 1:
        return [name, ""]
    return [name[:dot], name[dot + 1:].lower()]

names = ["report.final.pdf", "archive.tar.gz", ".bashrc", "Makefile", "photo.JPG", "notes.", "backup.TAR.BZ2", "README.md", "scan.pdf", "img.jpg", ".config.json"]
kinds = {}
for n in names:
    parts = split_ext(n)
    ext = "(none)" if parts[1] == "" else parts[1]
    kinds[ext] = kinds.get(ext, 0) + 1
    print(f"{n:<17} stem {parts[0]:<14} ext {ext}")
for k in sorted(kinds.keys()):
    print(f"{k:<8} {kinds[k]}")
