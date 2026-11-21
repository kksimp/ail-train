E = [("ana", ["maths", "physics", "art"]), ("ben", ["maths", "history"]), ("cai", ["physics", "chemistry"]), ("dee", ["art", "history", "music"]), ("eli", ["chemistry", "music"])]
cl = {}
for _, sub in E:
    for a in sub:
        cl.setdefault(a, set())
        for b in sub:
            if a != b: cl[a].add(b)
ex = sorted(sorted(cl), key=lambda x: -len(cl[x]))
sl = {}
for x in ex:
    used = {sl[o] for o in cl[x] if o in sl}; k = 0
    while k in used: k += 1
    sl[x] = k
for k in range(max(sl.values()) + 1): print(f"slot {k + 1}: {', '.join(sorted(x for x in ex if sl[x] == k))}")
