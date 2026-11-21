reigns = sorted([("Oswin I", 1012, 1049), ("Edda", 1049, 1061), ("Oswin II", 1058, 1090), ("Harald", 1094, 1101), ("Maud", 1101, 1135), ("Aelric", 1130, 1132), ("Tobin", 1139, 1175)], key=lambda r: r[1])
latest = reigns[0][2]
gaps = 0
for i in range(1, len(reigns)):
    name, start, end = reigns[i]
    if start < latest:
        print(f"co-regency: {name} joined in {start}, {latest - start} years of overlap")
    elif start > latest:
        gaps += start - latest
        print(f"interregnum {latest}-{start} before {name}")
    latest = max(latest, end)
longest = sorted(reigns, key=lambda r: r[1] - r[2])[0]
lengths = [r[2] - r[1] for r in reigns]
mean = sum(lengths) / len(lengths)
print(f"longest reign: {longest[0]}, {longest[2] - longest[1]} years")
print(f"mean reign {mean:.1f} years; dynasty {reigns[0][1]}-{latest}, {gaps} years without a ruler")
