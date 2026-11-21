class Cookie:
    def __init__(self, name, value, domain, path, secure, host_only):
        self.name, self.value, self.domain, self.path, self.secure, self.host_only = name, value, domain, path, secure, host_only

def store(jar, host, header):
    parts = [p.strip() for p in header.split(";")]
    eq = parts[0].find("=")
    c = Cookie(parts[0][:eq], parts[0][eq + 1:], host, "/", False, True)
    remove = False
    for attr in parts[1:]:
        kv = attr.split("=")
        key = kv[0].lower()
        if key == "path":
            c.path = kv[1]
        elif key == "domain":
            c.domain = kv[1]
            c.host_only = False
        elif key == "secure":
            c.secure = True
        elif key == "max-age" and kv[1] == "0":
            remove = True
    jar[:] = [o for o in jar if not (o.name == c.name and o.domain == c.domain and o.path == c.path)]
    if not remove:
        jar.append(c)

def domain_ok(c, host):
    if c.host_only:
        return host == c.domain
    return host == c.domain or host.endswith("." + c.domain)

def header_for(jar, url):
    scheme_end = url.find("://")
    https = url[:scheme_end] == "https"
    rest = url[scheme_end + 3:]
    slash = rest.find("/")
    if slash < 0:
        slash = len(rest)
    host = rest[:slash]
    path = rest[slash:] if slash < len(rest) else "/"
    sent = [c for c in jar if domain_ok(c, host) and path.startswith(c.path) and (https or not c.secure)]
    return "; ".join(f"{c.name}={c.value}" for c in sent)

jar = []
store(jar, "shop.example.com", "sid=abc123; Path=/; HttpOnly")
store(jar, "shop.example.com", "cart=3; Path=/cart; Max-Age=3600")
store(jar, "shop.example.com", "lang=en; Domain=example.com; Path=/")
store(jar, "shop.example.com", "token=xyz; Path=/; Secure")
store(jar, "shop.example.com", "cart=4; Path=/cart")
print(f"jar holds {len(jar)} cookies")
for url in ["https://shop.example.com/cart/view", "http://shop.example.com/", "http://blog.example.com/post", "https://other.org/"]:
    h = header_for(jar, url)
    shown = "(none)" if h == "" else h
    print(f"{url:<35} Cookie: {shown}")
store(jar, "shop.example.com", "cart=0; Path=/cart; Max-Age=0")
print(f"after delete: {header_for(jar, 'https://shop.example.com/cart/')}")
