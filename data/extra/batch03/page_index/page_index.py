P = ["Bees and flowers", "The hive and its queen", "Queen cells, drones", "Flowers in spring", "Honey and the hive", "Drones and the queen", "Wax and honey"]
def rg(p):
    out = []; i = 0
    while i < len(p):
        j = i
        while j + 1 < len(p) and p[j + 1] == p[j] + 1: j += 1
        out.append(f"{p[i]}-{p[j]}" if j > i else f"{p[i]}"); i = j + 1
    return ", ".join(out)
for t in sorted(["queen", "hive", "honey", "drones", "flowers", "wasps"]):
    f = [i + 1 for i, x in enumerate(P) if t in x.lower().replace(",", "").split(" ")]
    print(f"{t:<8} {rg(f) if f else '-'}")
