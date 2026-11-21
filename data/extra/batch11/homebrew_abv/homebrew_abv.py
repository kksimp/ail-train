batches = [("pale ale", 1052, 1011), ("stout", 1068, 1018), ("cider", 1055, 1000), ("barley wine", 1105, 1028), ("stuck batch", 1060, 1042)]
def abv(b):
    return float(b[1] - b[2]) * 131.25 / 1000.0
def attenuation(b):
    return float(b[1] - b[2]) / float(b[1] - 1000) * 100.0
for b in batches:
    att = attenuation(b)
    note = " (fermentation may have stalled)" if att < 65.0 else ""
    print(f"{b[0]:<12} OG 1.{b[1] - 1000:03} FG 1.{b[2] - 1000:03}: {abv(b):.2f}% ABV, attenuation {att:.1f}%{note}")
strongest = max(batches, key=lambda x: x[1] - x[2])
print(f"strongest: {strongest[0]}")
