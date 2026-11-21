configs = [{"host": "db.local", "port": "5432"}, {"host": "cache.local"}, {"port": "80"}, {"host": "api.local", "port": "eighty"}, {"host": "mail.local", "port": "587", "tls": "on"}]
usable = []
for i, c in enumerate(configs):
    ok = "host" in c
    port = None
    if ok:
        try:
            port = int(c.get("port", "443"))
        except ValueError:
            ok = False
    if ok:
        print(f"config {i + 1}: {c['host']}:{port}")
        usable.append(port)
    else:
        print(f"config {i + 1}: rejected ({len(c)} keys)")
print(f"{len(usable)} usable, {sum(1 for p in usable if p in (443, 587))} on secure ports")
