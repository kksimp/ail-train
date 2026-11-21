def load(t):
    s = {"port": 80, "host": "localhost", "debug": False}
    for i, raw in enumerate(t.split("\n")):
        l = raw.strip()
        if not l or l.startswith("#"): continue
        p = l.split("=")
        if len(p) != 2: return None, f"line {i + 1}: expected key=value"
        k, v = p[0].strip(), p[1].strip()
        if k == "port":
            if not v.lstrip("-").isdigit(): return None, f"line {i + 1}: bad port {v}"
            s["port"] = int(v)
        elif k == "host": s["host"] = v
        elif k == "debug":
            if v not in ("true", "false"): return None, f"line {i + 1}: not a bool: {v}"
            s["debug"] = v == "true"
        else: return None, f"line {i + 1}: unknown key {k}"
    return s, None
for c in ["# web\nport = 8080\nhost = example.org\ndebug = true", "port = 90\nhost = a.b\ndebug = yes", "port = 1\ncolour = red"]:
    s, e = load(c); print(f"ok: {s['host']}:{s['port']} debug={str(s['debug']).lower()}" if e is None else f"error: {e}")
