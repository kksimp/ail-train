rc = {}
kids = {}

def release(name, freed):
    rc[name] -= 1
    if rc[name] == 0:
        freed.append(name)
        for k in kids.get(name, []):
            release(k, freed)

links = [["root", "doc"], ["root", "cache"], ["root", "ring_a"], ["doc", "page1"], ["doc", "page2"], ["page1", "img"], ["cache", "img"], ["ring_a", "ring_b"], ["ring_b", "ring_a"]]
for l in links:
    kids.setdefault(l[0], []).append(l[1])
    rc[l[1]] = rc.get(l[1], 0) + 1
print("counts: " + " ".join(f"{k}={rc[k]}" for k in rc))
for name in ["doc", "cache", "ring_a"]:
    freed = []
    release(name, freed)
    lst = "nothing" if not freed else ", ".join(freed)
    print(f"root drops {name}: freed {lst}")
leaked = [f"{k} (count {v})" for k, v in rc.items() if v > 0]
print("leaked: " + ", ".join(leaked))
