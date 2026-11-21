tools = [None] * 3
def lend(slots, item, who):
    for i in range(len(slots)):
        if slots[i] is None:
            slots[i] = (item, who); return i
    return -1
for item, who in [("drill", "ana"), ("ladder", "ben"), ("saw", "cy"), ("sander", "dee")]:
    print(f"{who} borrows {item}: slot {lend(tools, item, who)}")
tools[1] = None
print(f"dee tries again: slot {lend(tools, 'sander', 'dee')}")
for i, s in enumerate(tools):
    if s is None: print(f"shelf {i}: free")
    else: print(f"shelf {i}: {s[0]} with {s[1]}")
bikes = [None, None]
print(f"eve takes bike 4471 from rack slot {lend(bikes, 4471, 'eve')}")
print(f"bike rack: {sum(1 for b in bikes if b is None)} of {len(bikes)} free")
