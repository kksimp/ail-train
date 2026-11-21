lines = ["north,jan,120", "south,jan,90", "north,feb,140", "east,jan,60", "south,feb,bad", "east,feb,75", "south,mar,110", "north,mar,", "east,mar,80"]
t = {}; sk = 0
for l in lines:
    p = l.split(",")
    try:
        a = int(p[2].strip()); t.setdefault(p[0], {}); t[p[0]][p[1]] = t[p[0]].get(p[1], 0) + a
    except ValueError: sk += 1
ms = ["jan", "feb", "mar"]
print(f"{'region':<6}" + "".join(f"{m:>5}" for m in ms) + "  total")
for r in sorted(t):
    print(f"{r:<6}" + "".join(f"{t[r].get(m, 0):>5}" for m in ms) + f"  {sum(t[r].values()):>5}")
print(f"skipped {sk}")
