orchard = [("Bramley", 3, True), ("Cox", 3, False), ("Discovery", 2, False), ("Egremont", 1, False), ("Jonagold", 4, True), ("Spartan", 5, False)]

def partners(t):
    return [o[0] for o in orchard if o[0] != t[0] and not o[2] and abs(o[1] - t[1]) <= 1]

lonely = []
for t in orchard:
    ps = partners(t)
    want = 2 if t[2] else 1
    mark = "ok" if len(ps) >= want else "SHORT"
    if len(ps) < want:
        lonely.append(t[0])
    names = "none" if not ps else ", ".join(ps)
    print(f"{t[0]:<9} group {t[1]}: {names} ({mark})")
for name in lonely:
    t = next(o for o in orchard if o[0] == name)
    print(f"{name} needs a diploid from group {max(t[1] - 1, 1)} to {t[1] + 1}")
