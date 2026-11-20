def mask(a):
    if a.count("@") != 1 or a.find("@") == 0:
        return None
    at = a.find("@")
    local, dom = a[:at], a[at + 1:]
    if "." not in dom:
        return None
    if len(local) <= 2:
        return "*" * len(local) + "@" + dom
    return local[0] + "*" * (len(local) - 2) + local[-1] + "@" + dom
for a in ["jane.doe@example.com", "al@site.org", "x@y.io", "nobody", "two@@signs.com", "@lost.net", "me@localhost"]:
    m = mask(a)
    print(f"{a:<22} {m if m is not None else '(invalid)'}")
doms = {}
for a in ["jane.doe@example.com", "bob@example.com", "al@site.org"]:
    d = a[a.find("@") + 1:]
    doms[d] = doms.get(d, 0) + 1
print("{" + ", ".join(f'"{k}": {v}' for k, v in doms.items()) + "}")
