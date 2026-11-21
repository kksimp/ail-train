chart = ["..xxxx....", ".xooooxx..", "xoo##ooox.", "xo####oox.", "xoo##ooox.", ".xooooox..", "..xxxxx...", "....|.....", "...||.....", "....|....."]
legend = {'x': "310 black", 'o': "666 red", '#': "726 yellow", '|': "699 green"}
per_skein = 25
counts = {}
for row in chart:
    for c in row:
        if c != '.':
            counts[c] = counts.get(c, 0) + 1
total = 0
for sym in sorted(counts.keys(), key=lambda k: -counts[k]):
    n = counts[sym]
    total += n
    skeins = (n + per_skein - 1) // per_skein
    thread = legend.get(sym, "unknown")
    print(f"{sym} {thread:<11} {n:>3} stitches, {skeins} skein(s)")
cells = len(chart) * len(chart[0])
print(f"{total} stitches on {cells} squares, {cells - total} left as fabric")
