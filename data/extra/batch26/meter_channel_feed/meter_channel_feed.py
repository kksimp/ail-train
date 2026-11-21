r = [4012, 4019, 4031, 4031, 4058, 4060]
for v in r: print(f"reading {v} kWh")
used = [b - a for a, b in zip(r, r[1:])]
print(f"hourly use: {used}")
print(f"peak hour {max(used)} kWh, idle hours {sum(1 for u in used if u == 0)}")
