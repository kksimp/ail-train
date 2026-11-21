ev = "click view click scroll view click buy view click scroll".split(" ")
c = {}; o = []
for e in ev:
    if e not in c: o.append(e)
    c[e] = c.get(e, 0) + 1
print("first seen order: [" + ", ".join(f'"{x}"' for x in o) + "]")
print(f"clicks {c['click']}, refunds 0")
print(" ".join(f"{k}={c[k]}" for k in sorted(o, key=lambda k: -c[k])))
