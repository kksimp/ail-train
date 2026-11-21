km = {"Hana": 21, "Iain": 13, "Jude": 30}
pledges = [("Hana", "Gran", 100, 0, 0, True), ("Hana", "Office", 0, 0, 5000, False), ("Iain", "Dad", 200, 2000, 0, True), ("Iain", "Neighbour", 50, 0, 0, False), ("Jude", "Aunt", 75, 2000, 0, True), ("Jude", "Coach", 0, 0, 1500, True), ("Jude", "Friend", 25, 0, 0, False)]

def amount(per_km, cap, fixed, k):
    if per_km == 0:
        return fixed
    raw = per_km * k
    return min(raw, cap) if cap > 0 else raw

def money(c):
    return f"{c // 100}.{c % 100:02d}"

grand = 0
for walker, dist in km.items():
    mine = [p for p in pledges if p[0] == walker]
    raised = aid = 0
    for p in mine:
        amt = amount(p[2], p[3], p[4], dist)
        raised += amt
        if p[5]:
            aid += amt // 4
    grand += raised + aid
    print(f"{walker:<5} {dist} km, {len(mine)} sponsors: {money(raised)} + gift aid {money(aid)} = {money(raised + aid)}")
print(f"raised in all: {money(grand)}")
