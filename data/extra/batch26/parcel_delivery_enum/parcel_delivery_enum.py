orders = [("C", 8), ("C", 34), ("L", "Elm St", "L"), ("L", "Mill Rd", "S"), ("P",), ("D", 1500), ("D", 2600)]
def fee(o):
    if o[0] == "C":
        return 650 + (o[1] - 20) * 25 if o[1] > 20 else 650
    if o[0] == "L":
        return 420 if o[2] == "L" else 299
    if o[0] == "P":
        return 0
    return -1 if o[1] > 2000 else 899
def desc(o):
    if o[0] == "C": return f"courier {o[1]} km"
    if o[0] == "L": return f"locker {o[1]} ({o[2]})"
    if o[0] == "P": return "store pickup"
    return f"drone {o[1]} g"
def money(c): return f"{c // 100}.{c % 100:02}"
total = 0; refused = 0
for o in orders:
    f = fee(o); t = desc(o)
    if f < 0:
        print(f"{t:<20} not possible"); refused += 1; continue
    total += f
    print(f"{t:<20} {money(f):>6}")
print(f"fees {money(total)}, {refused} refused")
