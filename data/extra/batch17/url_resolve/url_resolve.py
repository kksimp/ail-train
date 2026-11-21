def remove_dots(p):
    segs = p.split("/")
    out = []
    for i, s in enumerate(segs):
        last = i == len(segs) - 1
        if s == ".":
            if last:
                out.append("")
        elif s == "..":
            if len(out) > 1:
                out = out[:-1]
            if last:
                out.append("")
        else:
            out.append(s)
    return "/".join(out)

def resolve(scheme, host, path, query, raw):
    r = raw
    frag = ""
    at = r.find("#")
    if at >= 0:
        frag = r[at:]
        r = r[:at]
    q = ""
    at = r.find("?")
    if at >= 0:
        q = r[at:]
        r = r[:at]
    if ":" in r:
        return raw
    if r.startswith("//"):
        rest = r[2:]
        cut = rest.find("/")
        if cut < 0:
            cut = len(rest)
        return f"{scheme}://{rest[:cut]}{remove_dots(rest[cut:])}{q}{frag}"
    if r == "":
        use_q = query if q == "" else q
        return f"{scheme}://{host}{path}{use_q}{frag}"
    if r.startswith("/"):
        return f"{scheme}://{host}{remove_dots(r)}{q}{frag}"
    dir_end = max(path.rfind("/"), 0) + 1
    merged = path[:dir_end] + r
    return f"{scheme}://{host}{remove_dots(merged)}{q}{frag}"

print("base http://a/b/c/d;p?q")
refs = ["g", "./g", "g/", "/g", "//g", "?y", "g?y", "#s", "g;x?y#s", "", ".", "../g", "../../../g", "g:h"]
for r in refs:
    full = resolve("http", "a", "/b/c/d;p", "?q", r)
    shown = "(empty)" if r == "" else r
    print(f"{shown:<10} -> {full}")
