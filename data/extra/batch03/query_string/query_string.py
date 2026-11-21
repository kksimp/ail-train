def dec(t):
    out = ""; i = 0
    while i < len(t):
        c = t[i]
        if c == "+": out += " "
        elif c == "%" and i + 2 < len(t): out += chr(int(t[i + 1:i + 3], 16)); i += 2
        else: out += c
        i += 1
    return out
m = {}
for p in "name=Ada+Lovelace&lang=en&note=50%25+off%21&lang=fr&flag&empty=".split("&"):
    if not p: continue
    e = p.find("="); e = len(p) if e < 0 else e
    m[dec(p[:e])] = dec(p[e + 1:]) if e < len(p) else ""
for k in sorted(m): print(f'{k} = "{m[k]}"')
