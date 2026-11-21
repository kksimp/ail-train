def pu(t):
    i = t.find("://")
    if i < 0: return None
    sc = t[:i]; rest = t[i + 3:]
    sl = rest.find("/"); sl = len(rest) if sl < 0 else sl
    au = rest[:sl]; tail = rest[sl:]; q = ""
    if "?" in tail: k = tail.find("?"); q = tail[k + 1:]; tail = tail[:k]
    path = tail or "/"
    host, port = au, 443 if sc == "https" else 80
    if ":" in au:
        c = au.find(":"); host = au[:c]
        try: port = int(au[c + 1:])
        except ValueError: return None
    return sc, host, port, path, q
for t in ["https://example.org/docs/intro?lang=en", "http://localhost:8080", "https://shop.test:8443/cart", "ftp://files.test/pub/", "example.org/no-scheme", "http://bad:port/x"]:
    u = pu(t)
    print(" | ".join(map(str, u)) if u else f"cannot parse {t}")
