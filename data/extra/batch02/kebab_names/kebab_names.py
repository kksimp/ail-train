def wo(n):
    out, cur, pl = [], "", False
    for c in n:
        if c in "_- ":
            if cur: out.append(cur); cur = ""
        elif c.isupper() and pl:
            out.append(cur); cur = c.lower()
        else:
            cur += c.lower()
        pl = c.islower()
    if cur: out.append(cur)
    return out
def camel(n):
    ws = wo(n)
    return "".join(w if i == 0 else w[:1].upper() + w[1:] for i, w in enumerate(ws))
for n in ["userName", "HTTPServer", "max_retry_count", "  Total Price ", "already-kebab", "x"]:
    print(f"{n:<18} {'-'.join(wo(n)):<18} {camel(n)}")
