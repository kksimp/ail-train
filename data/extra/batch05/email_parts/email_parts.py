def nm(a):
    p = a.strip().lower().split("@")
    if len(p) != 2 or not p[0] or "." not in p[1]: return None
    return p[0].split("+")[0] + "@" + p[1]
s = set()
for a in ["Ann+news@Example.com", " bob@mail.org ", "carl@localhost", "dee@@x.io", "ann@example.com", "@nouser.net", "Eve+a+b@Shop.co.uk"]:
    n = nm(a)
    if n: f = n not in s; s.add(n); print(f"{a.strip()} -> {n}{'' if f else ' (duplicate)'}")
    else: print(f"{a.strip()} -> invalid")
print(f"{len(s)} unique")
