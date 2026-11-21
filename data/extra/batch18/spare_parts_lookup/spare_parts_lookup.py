van = {"fuse 13A": 6, "valve seal": 0, "thermostat": 1}
depot = {"valve seal": 14, "pump": 2, "fan motor": 0}
lead = {"fan motor": 5, "pump": 3, "control board": 12}
def src(p):
    if van.get(p, 0) > 0: return f"in the van ({van[p]} left)"
    if depot.get(p, 0) > 0: return f"at the depot ({depot[p]} there)"
    if p in lead: return f"order it, {lead[p]} days"
    return "unknown part"
needs = ["fuse 13A", "valve seal", "fan motor", "control board", "gasket", "thermostat"]
for p in needs: print(f"{p:<13} {src(p)}")
print(f"{sum(1 for p in needs if van.get(p, 0) + depot.get(p, 0) > 0)} of {len(needs)} parts on hand today")
