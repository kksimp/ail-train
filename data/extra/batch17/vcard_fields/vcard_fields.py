class Prop:
    def __init__(self, name, params, value):
        self.name, self.params, self.value = name, params, value

def unfold(lines):
    out = []
    for l in lines:
        if l.startswith(" ") and len(out) > 0:
            out[-1] = out[-1] + l[1:]
        else:
            out.append(l)
    return out

def parse_prop(line):
    colon = line.find(":")
    if colon < 0:
        colon = len(line)
    head = line[:colon]
    value = line[min(colon + 1, len(line)):]
    semi = head.find(";")
    if semi < 0:
        semi = len(head)
    params = head[semi + 1:] if semi < len(head) else ""
    return Prop(head[:semi].upper(), params, value)

raw = ["BEGIN:VCARD", "FN:Ada Lovelace", "TEL;TYPE=work:+44 20 7946 0001", "TEL;TYPE=cell:+44 7700 900123", "EMAIL:ada@example.org", "NOTE:Wrote the first published program for", "  the Analytical Engine.", "END:VCARD", "BEGIN:VCARD", "FN:Alan Turing", "tel;type=home:+44 161 496 0000", "END:VCARD"]
lines = unfold(raw)
print(f"{len(raw)} raw lines, {len(lines)} after unfolding")
count = 0
for l in lines:
    p = parse_prop(l)
    if p.name == "BEGIN":
        count += 1
    elif p.name == "FN":
        print(f"contact {count}: {p.value}")
    elif p.name == "TEL":
        low = p.params.lower()
        kind = low[5:] if low.startswith("type=") else "other"
        print(f"  phone ({kind}): {p.value}")
    elif p.name == "EMAIL":
        print(f"  email: {p.value}")
    elif p.name == "NOTE":
        print(f"  note: {p.value}")
