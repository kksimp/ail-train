def nm(e):
    if "@" not in e: return e.lower()
    a = e.find("@"); l = e[:a].lower(); d = e[a + 1:].lower()
    if d == "mail.test":
        p = l.find("+"); l = (l[:p] if p >= 0 else l).replace(".", "")
    return f"{l}@{d}"
f = {}; o = []
for e in ["Jo.Smith@mail.test", "josmith+news@mail.test", "jo.smith@other.test", "JOSMITH@MAIL.TEST", "Ann@other.test", "ann@Other.test", "a.n.n@mail.test", "bad-address"]:
    k = nm(e)
    if k in f: print(f"duplicate: {e} (same as {f[k]})")
    else: f[k] = e; o.append(k)
print(f"{len(o)} unique: {', '.join(f[k] for k in o)}")
