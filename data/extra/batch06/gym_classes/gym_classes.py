C = {"spin": 3, "yoga": 2}; R = {"spin": [], "yoga": []}; W = {"spin": [], "yoga": []}
for e in ["book spin Ana", "book spin Ben", "book yoga Cat", "book spin Dan", "book spin Eve", "book yoga Fay", "book yoga Gus", "cancel spin Ben", "cancel yoga Cat", "book spin Hal", "cancel spin Ana"]:
    a, c, w = e.split(" ")
    if a == "book":
        if len(R[c]) < C[c]: R[c].append(w); print(f"{w} booked {c}")
        else: W[c].append(w); print(f"{w} waitlisted for {c}")
    else:
        R[c] = [p for p in R[c] if p != w]; print(f"{w} cancelled {c}")
        if W[c]: n = W[c].pop(0); R[c].append(n); print(f"  {n} moved up")
for c in ["spin", "yoga"]: print(f"{c}: {', '.join(R[c])} | waiting: {', '.join(W[c]) or 'none'}")
