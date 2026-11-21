def clock(m): return f"{m // 60:02}:{m % 60:02}"
prog = [("w", 1, 12), ("w", 2, 8), ("p", 15), ("s", 3, "soil wet"), ("w", 1, 6), ("w", 4, 20)]
now = 360; pz = {}
for s in prog:
    if s[0] == "w":
        print(f"{clock(now)} zone {s[1]} on for {s[2]} min"); pz[s[1]] = pz.get(s[1], 0) + s[2]; now += s[2]
    elif s[0] == "p":
        print(f"{clock(now)} pause {s[1]} min"); now += s[1]
    else: print(f"{clock(now)} skip zone {s[1]}: {s[2]}")
print(f"finished at {clock(now)}")
for z in sorted(pz): print(f"zone {z}: {pz[z]} min")
