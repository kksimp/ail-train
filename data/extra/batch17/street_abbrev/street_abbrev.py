def short_forms():
    return {"STREET": "ST", "AVENUE": "AVE", "ROAD": "RD", "BOULEVARD": "BLVD", "DRIVE": "DR", "LANE": "LN", "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W", "NORTHEAST": "NE", "APARTMENT": "APT", "SUITE": "STE", "FLOOR": "FL"}

def normalise(addr, table):
    cleaned = addr.upper().replace(".", "").replace(",", " ")
    words = [table.get(w, w) for w in cleaned.split()]
    return " ".join(words)

table = short_forms()
addrs = ["123 North Main Street, Apt. 4", "123 N. Main St Apt 4", "45 Ocean Boulevard Suite 200", "45 ocean blvd., ste 200", "9 West Lane", "9 W Ln Floor 2", "77 Northeast Park Drive"]
groups = {}
for i, a in enumerate(addrs):
    n = normalise(a, table)
    print(f"{i + 1}. {n}")
    groups.setdefault(n, []).append(i + 1)
for n, ids in groups.items():
    if len(ids) > 1:
        print(f"same address: {ids}")
print(f"{len(addrs)} entries, {len(groups)} distinct")
