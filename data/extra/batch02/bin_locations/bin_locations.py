bins = {}
for e in ["A1 bolt", "A1 nut", "A2 washer", "B1 bolt", "B1 hinge", "C3 nut"]:
    a, b = e.split(" "); bins.setdefault(a, []).append(b)
for cmd in ["pick A1 nut", "move A2 washer B1", "pick C3 nut", "pick C3 nut", "add D4 bracket"]:
    w = cmd.split(" ")
    if w[0] == "pick":
        if w[2] not in bins.get(w[1], []):
            print(f"{cmd}: not there"); continue
        bins[w[1]].remove(w[2])
        if not bins[w[1]]: del bins[w[1]]
    elif w[0] == "move":
        if w[2] in bins.get(w[1], []):
            bins[w[1]].remove(w[2]); bins.setdefault(w[3], []).append(w[2])
            if not bins[w[1]]: del bins[w[1]]
    elif w[0] == "add":
        bins.setdefault(w[1], []).append(w[2])
    print(f"{cmd}: ok")
for b in sorted(bins):
    print(f"{b}: {', '.join(bins[b])}")
print("bolt in: " + " ".join(sorted(b for b in bins if "bolt" in bins[b])))
