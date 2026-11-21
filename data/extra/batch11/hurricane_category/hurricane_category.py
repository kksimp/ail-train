def category(kmh):
    if kmh <= 62: return "tropical depression"
    if kmh <= 118: return "tropical storm"
    if kmh <= 153: return "category 1"
    if kmh <= 177: return "category 2"
    if kmh <= 208: return "category 3"
    if kmh <= 251: return "category 4"
    return "category 5"
track = [("Mon 00h", 30), ("Mon 12h", 55), ("Tue 00h", 70), ("Tue 12h", 95), ("Wed 00h", 125), ("Wed 12h", 140), ("Thu 00h", 110), ("Thu 12h", 60)]
peak = 0
peak_at = ""
for when, knots in track:
    kmh = int(float(knots) * 1.852)
    if kmh > peak:
        peak = kmh
        peak_at = when
    print(f"{when}: {knots:>3} kt = {kmh:>3} km/h, {category(kmh)}")
print(f"peak {peak} km/h on {peak_at}: {category(peak)}")
