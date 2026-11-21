def to_int(s):
    t = s[1:] if s.startswith("-") else s
    return int(s) if t.isdigit() and t != "" else None

def key_of(var):
    rest = var[4:] if var.startswith("APP_") else ""
    return rest.lower().replace("__", ".")

def convert(default, raw):
    if default == "true" or default == "false":
        low = raw.lower()
        if low in ("1", "yes", "true"):
            return "true", None
        if low in ("0", "no", "false"):
            return "false", None
        return None, f"'{raw}' is not a yes/no value"
    if to_int(default) is not None:
        n = to_int(raw.strip())
        if n is None:
            return None, f"'{raw}' is not a whole number"
        return f"{n}", None
    return raw, None

settings = {"db.pool_size": "4", "db.host": "localhost", "server.debug": "false", "server.port": "8080", "cache.ttl": "60"}
env = [("APP_DB__POOL_SIZE", "16"), ("APP_SERVER__DEBUG", "yes"), ("HOME", "/root"), ("APP_SERVER__PORT", "80a"), ("APP_DB__HOST", "db.internal"), ("APP_CACHE__SIZE", "512"), ("APP_CACHE__TTL", " 300 ")]
for var, raw in env:
    key = key_of(var)
    if key == "":
        continue
    old = settings.get(key, "")
    if old == "":
        print(f"{var:<18} -> {key}: no such setting, ignored")
        continue
    v, err = convert(old, raw)
    if v is not None:
        settings[key] = v
        print(f"{var:<18} -> {key}: {old} -> {v}")
    else:
        print(f"{var:<18} -> {key}: rejected, {err}")
for k in sorted(settings.keys()):
    print(f"  {k} = {settings[k]}")
