def clean(raw):
    name = raw.strip().lower()
    if len(name) < 3: return (None, "too short")
    if len(name) > 12: return (None, f"too long ({len(name)} chars)")
    if not name[0].isalpha(): return (None, "must start with a letter")
    for c in name:
        if not (c.isalnum() or c == "_"):
            return (None, f"bad character '{c}'")
    return (name, None)
raws = ["  Mira_K ", "jo", "Zed99", "9lives", "anna.b", "ThisNameIsWayTooLong", "ZED99", "sam"]
taken = []; refused = 0
for r in raws:
    n, e = clean(r)
    if e:
        print(f"refused '{r}': {e}"); refused += 1; continue
    if n in taken:
        print(f"refused '{r}': {n} is taken"); refused += 1; continue
    taken.append(n)
    print(f"welcome {n}")
print(f"{len(taken)} accounts made, {refused} refused")
