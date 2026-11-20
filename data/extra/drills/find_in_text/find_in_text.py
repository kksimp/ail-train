def dir_of(p):
    cut = p.rfind("/")
    if cut < 0:
        return "."
    if cut == 0:
        return "/"
    return p[:cut]

def base_of(p):
    cut = p.rfind("/")
    return p if cut < 0 else p[cut + 1:]

def ext_of(p):
    name = base_of(p)
    dot = name.rfind(".")
    if dot <= 0:
        return ""
    return name[dot + 1:]

def first_segment(p):
    cut = p.find("/")
    return p if cut < 0 else p[:cut]

for p in ["src/store/report.ail", "/etc/hosts", "notes.txt", "a/b/.hidden", "/top"]:
    print(f"{p}: dir={dir_of(p)} base={base_of(p)} ext=[{ext_of(p)}] depth={p.count('/')}")
print(first_segment("src/store/report.ail"))
print(first_segment("plain"))
print("a ?")
print("banana".find("an"))
print("banana".rfind("an"))
print("banana".find("x"))
