tmpl = ["passport", "charger", "toothbrush", "tickets"]
def report(trip, items, done):
    print(f"{trip}: {len(items)} items, still to pack: {', '.join(i for i in items if i not in done)}")
report("beach", tmpl + ["sunscreen"], {"passport", "tickets"})
report("ski", tmpl + ["gloves", "goggles"], {"charger", "gloves"})
report("template", tmpl, set())
