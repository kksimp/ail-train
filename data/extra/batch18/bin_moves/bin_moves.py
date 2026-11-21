bins = {"A-01": ["bolt-m6", 120, 200], "A-02": ["nut-m6", 40, 200], "B-07": ["washer", 500, 600]}
bins["A-02"][1] += 100
print(f"copy emptied, A-01 keeps {bins['A-01'][1]}")
bins["B-07"][1] -= 150
bins["C-03"] = ["washer", 150, 300]
for c, b in bins.items(): print(f"{c} {b[0]:<8} {b[1]:>4}/{b[2]} ({b[1] * 100 // b[2]}% full)")
print(f"washers in all bins: {sum(b[1] for b in bins.values() if b[0] == 'washer')}, copy has 0")
