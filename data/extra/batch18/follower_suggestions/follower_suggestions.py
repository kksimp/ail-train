fo = {"ana": {"ben", "cy", "dot"}, "ben": {"ana", "eli"}, "cy": {"ana", "eli", "fay"}, "dot": {"fay"}, "eli": {"ben"}, "fay": {"cy"}}
mine = fo["ana"]
mu = [p for p in sorted(mine) if "ana" in fo.get(p, set())]
print("ana and mutual: [" + ", ".join(f'"{x}"' for x in mu) + "]")
v = {}
for f in sorted(mine):
    for s in sorted(fo.get(f, set()) - mine):
        if s != "ana": v[s] = v.get(s, 0) + 1
for s in sorted(sorted(v), key=lambda k: -v[k]): print(f"suggest {s}: followed by {v[s]} of your follows")
print(f"ana and cy together follow {len(mine | fo['cy'])} people")
