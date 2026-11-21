def runs(cells):
    out = []; n = 0
    for c in cells:
        if c == "#": n += 1
        elif n > 0: out.append(n); n = 0
    if n > 0: out.append(n)
    return "0" if not out else " ".join(str(x) for x in out)
pic = [".##.##.", "#######", "#######", ".#####.", "..###..", "...#...", "......."]
for r in pic: print(f"{r}  {runs(r)}")
print("columns: " + " | ".join(runs([pic[r][c] for r in range(len(pic))]) for c in range(len(pic[0]))))
