members = ["Ada", "Bo", "Cy", "Di", "Ed"]
roles = ["chair", "secretary", "treasurer"]
past = {}
served = {}
for year in range(2024, 2030):
    taken = set()
    parts = []
    for role in roles:
        blocked = past.get(role, [])[-3:]
        free = [m for m in members if m not in taken and m not in blocked]
        if not free:
            parts.append(f"{role} vacant")
            continue
        who = min(free, key=lambda m: (served.get(m, 0), members.index(m)))
        taken.add(who)
        served[who] = served.get(who, 0) + 1
        past.setdefault(role, []).append(who)
        parts.append(f"{role} {who}")
    print(f"{year}: {', '.join(parts)}")
for m in members:
    print(f"{m}: {served.get(m, 0)} terms")
