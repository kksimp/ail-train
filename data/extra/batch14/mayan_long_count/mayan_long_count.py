def jdn(y, m, d):
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
tz = ["Imix", "Ik", "Akbal", "Kan", "Chicchan", "Cimi", "Manik", "Lamat", "Muluc", "Oc", "Chuen", "Eb", "Ben", "Ix", "Men", "Cib", "Caban", "Etznab", "Cauac", "Ahau"]
haab = ["Pop", "Uo", "Zip", "Zotz", "Tzec", "Xul", "Yaxkin", "Mol", "Chen", "Yax", "Zac", "Ceh", "Mac", "Kankin", "Muan", "Pax", "Kayab", "Cumku", "Uayeb"]
for y, m, d in [[2012, 12, 21], [2026, 11, 21], [1969, 7, 20], [2000, 1, 1], [1500, 6, 15]]:
    days = jdn(y, m, d) - 584283
    lc = [days // 144000, days // 7200 % 20, days // 360 % 20, days // 20 % 18, days % 20]
    long = ".".join(str(v) for v in lc)
    tn = (days + 3) % 13 + 1
    tname = tz[(days + 19) % 20]
    h = (days + 348) % 365
    print(f"{y}-{m:02}-{d:02}: day {days}, long count {long}, {tn} {tname} {h % 20} {haab[h // 20]}")
print("the Calendar Round (Tzolkin and Haab together) repeats every lcm(260, 365) = 18980 days")
