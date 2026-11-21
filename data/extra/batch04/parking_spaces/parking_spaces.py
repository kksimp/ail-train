used = {}
for e in ["in AB12", "in CD34", "in EF56", "out CD34", "in GH78", "in IJ90", "in KL11", "in MN22", "in OP33", "out AB12", "in QR44"]:
    a, p = e.split(" ")
    if a == "in":
        b = next((b for b in range(1, 7) if b not in used), -1)
        if b < 0: print(f"{p}: full, turned away")
        else: used[b] = p; print(f"{p}: bay {b}")
    else:
        f = next((b for b in used if used[b] == p), -1)
        if f > 0: del used[f]; print(f"{p}: left bay {f}")
print(" ".join(f"{b}:{used.get(b, '-')}" for b in range(1, 7)))
