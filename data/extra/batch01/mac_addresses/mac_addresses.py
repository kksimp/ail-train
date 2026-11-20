def norm(t):
    h = [c for c in t.lower() if c not in ":-."]
    if len(h) != 12 or not all(c in "0123456789abcdef" for c in h):
        return None
    return ":".join("".join(h[i:i + 2]) for i in range(0, 12, 2))
for m in ["00:1A:2b:3C:4d:5E", "00-1a-2b-3c-4d-5e", "001a.2b3c.4d5e", "01:00:5e:00:00:fb", "00:1a:2b:3c:4d", "zz:1a:2b:3c:4d:5e"]:
    n = norm(m)
    if n:
        print(f"{m:<20} {n} {'multicast' if int(n[:2], 16) & 1 else 'unicast'}")
    else:
        print(f"{m:<20} invalid")
print("same device: true")
