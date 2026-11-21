V = [("Rex", "dog", "vaccine"), ("Tom", "cat", "check-up"), ("Bun", "rabbit", "teeth"), ("Rex", "dog", "limp"), ("Ivy", "cat", "vaccine"), ("Max", "dog", "vaccine"), ("Tom", "cat", "vaccine")]
bs = {}
for p, s, r in V:
    bs.setdefault(s, [])
    if p not in bs[s]: bs[s].append(p)
for s in sorted(bs): print(f"{s}: {', '.join(bs[s])}")
rc = {}
for v in V: rc[v[2]] = rc.get(v[2], 0) + 1
t = max(rc, key=lambda k: rc[k]); print(f"most common reason: {t} ({rc[t]})")
pc = {}
for v in V: pc[v[0]] = pc.get(v[0], 0) + 1
print("seen more than once: [" + ", ".join(f'"{p}"' for p in sorted(pc) if pc[p] > 1) + "]")
