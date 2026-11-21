def kd(c):
    if c.isdigit(): return "number"
    if c.isalpha() or c == "_": return "name"
    if c in "()": return "bracket"
    return "operator"
def tk(s):
    o = []; i = 0
    while i < len(s):
        if s[i] == " ": i += 1; continue
        k = kd(s[i]); j = i + 1
        if k in ("number", "name"):
            while j < len(s) and kd(s[j]) == k and s[j] != " ": j += 1
        o.append((k, s[i:j])); i = j
    return o
for e in ["3 + 41 * x", "(rate_b - 7) / total", "max(a, 10) ^ 2"]:
    t = tk(e); print(f"{e} => " + " | ".join(x[1] for x in t)); c = {}
    for x in t: c[x[0]] = c.get(x[0], 0) + 1
    print("  " + " ".join(f"{k}={c[k]}" for k in sorted(c)))
