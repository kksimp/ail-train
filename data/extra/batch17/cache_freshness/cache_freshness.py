def directives(h):
    out = {}
    for part in h.split(","):
        p = part.strip().lower()
        if p == "":
            continue
        eq = p.find("=")
        if eq < 0:
            out[p] = -1
        else:
            v = p[eq + 1:]
            out[p[:eq]] = int(v) if v.isdigit() else 0
    return out

def verdict(cc, age, resident):
    d = directives(cc)
    if "no-store" in d:
        return "not stored"
    if "no-cache" in d:
        return "stored, revalidate every time"
    lifetime = d["s-maxage"] if "s-maxage" in d else d["max-age"] if "max-age" in d else 0
    current = age + resident
    if lifetime > current:
        return f"fresh for {lifetime - current} more s"
    return f"stale by {current - lifetime} s"

cases = [("public, max-age=600", 30, 200), ("max-age=600, s-maxage=60", 0, 90), ("no-store", 0, 0), ("no-cache, max-age=3600", 10, 5), ("private, max-age=300", 280, 30), ("MAX-AGE=86400", 3600, 7200), ("", 0, 10)]
for cc, age, resident in cases:
    shown = "(none)" if cc == "" else cc
    print(f"{shown:<26} age {age:>4}+{resident:<4} {verdict(cc, age, resident)}")
