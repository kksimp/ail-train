zone = {"www.shop.test": ["CNAME", "shop.cdn.test"], "shop.cdn.test": ["CNAME", "edge7.cdn.test"], "edge7.cdn.test": ["A", "198.51.100.7"], "api.shop.test": ["A", "198.51.100.20"], "old.shop.test": ["CNAME", "legacy.shop.test"], "legacy.shop.test": ["CNAME", "old.shop.test"], "blog.shop.test": ["CNAME", "gone.host.test"]}
cache = {}

def resolve(name):
    if name in cache:
        return f"{cache[name]} (cached)", None
    cur = name
    seen = set()
    path = []
    for i in range(8):
        if cur in seen:
            return None, f"loop at {cur}"
        seen.add(cur)
        if cur not in zone:
            return None, f"no record for {cur}"
        rec = zone[cur]
        if rec[0] == "A":
            cache[name] = rec[1]
            path.append(rec[1])
            return " > ".join(path), None
        path.append(rec[1])
        cur = rec[1]
    return None, "chain too long"

for name in ["www.shop.test", "api.shop.test", "old.shop.test", "blog.shop.test", "www.shop.test"]:
    answer, err = resolve(name)
    if err is None:
        print(f"{name}: {answer}")
    else:
        print(f"{name}: error, {err}")
print(f"{len(cache)} names cached")
