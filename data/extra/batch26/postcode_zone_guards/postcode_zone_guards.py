def zone(pc):
    p = pc.strip().upper()
    if p.startswith("BT"): return "Northern Ireland"
    if p.startswith(("HS", "ZE", "KW")): return "Highlands and Islands"
    if p.startswith(("JE", "GY")): return "Channel Islands"
    if p.startswith("IM"): return "Isle of Man"
    return "mainland"
rate = {"Northern Ireland": 695, "Highlands and Islands": 895, "Channel Islands": 1095, "Isle of Man": 795}
bz = {}
for o in ["sw1a 1aa", "BT7 1NN", "HS2 9AB", "JE2 3XP", "M1 1AE", "KW15 1HR", "IM1 2AA", "EH1 1YZ"]:
    z = zone(o); r = rate.get(z, 395)
    bz[z] = bz.get(z, 0) + r
    print(f"{o.upper():<9} {z:<22} {r // 100}.{r % 100:02}")
for z, c in bz.items():
    print(f"{z}: {c // 100}.{c % 100:02}")
