cap = {"pier": 4, "park": 3, "mill": 2}
b = {"pier": 2, "park": 3, "mill": 0}
ev = [("H", "pier"), ("R", "mill"), ("R", "park"), ("H", "mill"), ("H", "mill"), ("H", "pier"), ("H", "pier"), ("R", "pier")]
r = 0
for k, d in ev:
    if k == "H":
        if b[d] == 0: print(f"hire at {d}: empty"); r += 1
        else: b[d] -= 1
    else:
        if b[d] == cap[d]: print(f"return at {d}: full"); r += 1
        else: b[d] += 1
for d in ["pier", "park", "mill"]: print(f"{d}: {b[d]}/{cap[d]}")
print(f"refused {r}")
