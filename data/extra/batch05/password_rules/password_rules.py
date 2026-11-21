def pr(p):
    o = []
    if len(p) < 10: o.append("too short")
    if not any(c.isupper() for c in p): o.append("no capital")
    if not any(c.isdigit() for c in p): o.append("no digit")
    if all(c.isalnum() for c in p): o.append("no symbol")
    for i in range(2, len(p)):
        if p[i] == p[i - 1] == p[i - 2]: o.append(f"triple {p[i]}"); break
    return o
for p in ["hunter2", "CorrectHorse9!", "aaaBBB111###", "Pa55w0rd", "tr0ub4dor&3X"]:
    x = pr(p); print(f"{p}: ok" if not x else f"{p}: {', '.join(x)}")
