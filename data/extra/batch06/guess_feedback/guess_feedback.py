def mk(g, a):
    r = ["."] * 5; sp = {}
    for i in range(5):
        if g[i] == a[i]: r[i] = "G"
        else: sp[a[i]] = sp.get(a[i], 0) + 1
    for i in range(5):
        if r[i] == "." and sp.get(g[i], 0) > 0: r[i] = "Y"; sp[g[i]] -= 1
    return "".join(r)
for g in ["slate", "nacre", "eerie", "crane", "added", "caner"]: m = mk(g, "crane"); print(f"{g} {m}{' solved' if m == 'GGGGG' else ''}")
print(f"{mk('speed', 'abide')} for speed vs abide")
