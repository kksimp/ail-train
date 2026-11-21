class Field:
    def __init__(self, name, frm, upto):
        self.name, self.frm, self.upto = name, frm, upto

def money(cents):
    return f"{cents // 100}.{cents % 100:02}"

layout = [Field("id", 0, 4), Field("name", 4, 16), Field("amount", 16, 24), Field("date", 24, 32)]
width = layout[-1].upto
lines = ["0001Ada Lovelace0001234520250301", "0002Alan Turing 0000099920250302", "0003Grace       0010000020250315", "0004short", "0005Edsger      0000050020250401"]
total = 0
for line in lines:
    if len(line) != width:
        print(f"rejected: length {len(line)}, expected {width}")
        continue
    rec = {}
    for f in layout:
        rec[f.name] = line[f.frm:f.upto].strip()
    cents = int(rec["amount"])
    total += cents
    d = rec["date"]
    iso = f"{d[0:4]}-{d[4:6]}-{d[6:8]}"
    id_ = int(rec["id"])
    print(f"#{id_} {rec['name']:<12} {money(cents):>8} {iso}")
print(f"total {money(total)}")
