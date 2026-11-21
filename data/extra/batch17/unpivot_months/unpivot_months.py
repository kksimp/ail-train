class Cell:
    def __init__(self, region, month, value):
        self.region, self.month, self.value = region, month, value

def melt(header, rows):
    out = []
    for r in rows:
        for j in range(1, len(header)):
            if r[j] != "":
                out.append(Cell(r[0], header[j], int(r[j])))
    return out

header = ["region", "jan", "feb", "mar", "apr"]
rows = [["north", "120", "135", "", "150"], ["south", "90", "", "110", "95"], ["east", "200", "180", "210", ""], ["west", "", "60", "75", "80"]]
long = melt(header, rows)
print(f"{len(long)} long rows from {len(rows)} wide rows")
for c in long[:4]:
    print(f"  {c.region},{c.month},{c.value}")
by_month = {}
by_region = {}
for c in long:
    by_month[c.month] = by_month.get(c.month, 0) + c.value
    by_region[c.region] = by_region.get(c.region, 0) + c.value
for m, v in by_month.items():
    print(f"{m} total {v:>4}")
ranked = sorted(by_region.keys(), key=lambda k: -by_region[k])
shown = ", ".join(f"{k} {by_region[k]}" for k in ranked)
print(f"regions: {shown}")
