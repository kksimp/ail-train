c = {"bolts": 120, "nuts": 300, "hinges": 18}
for k, d in [("bolts", -50), ("hinges", -20), ("nuts", -290), ("hinges", 40), ("washers", 500), ("bolts", -60)]:
    h = c.get(k, 0)
    if h + d < 0: print(f"refused: pick {-d} {k}, only {h}"); continue
    c[k] = h + d
for k in sorted(c): print(f"{k:<8} {c[k]:>4}" + ("  low" if c[k] < 20 else ""))
