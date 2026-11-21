def jdn(y, m, d):
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045

def convert(j, epoch, months):
    year = (4 * (j - epoch) + 1463) // 1461
    start = epoch + 365 * (year - 1) + year // 4
    month = (j - start) // 30 + 1
    day = j - start - 30 * (month - 1) + 1
    return f"{day} {months[month - 1]} {year}"

coptic = ["Thout", "Paopi", "Hathor", "Koiak", "Tobi", "Meshir", "Paremhat", "Parmouti", "Pashons", "Paoni", "Epip", "Mesori", "Nasie"]
ethiopian = ["Meskerem", "Tikimt", "Hidar", "Tahsas", "Tir", "Yekatit", "Megabit", "Miyazya", "Ginbot", "Sene", "Hamle", "Nehase", "Pagume"]
dates = [(2023, 9, 11), (2023, 9, 12), (2024, 1, 7), (2024, 9, 11), (2025, 9, 6), (2026, 11, 21), (2000, 1, 1)]
for y, m, d in dates:
    j = jdn(y, m, d)
    c = convert(j, 1825030, coptic)
    e = convert(j, 1724221, ethiopian)
    print(f"{y}-{m:02}-{d:02}  Coptic {c:<20} Ethiopian {e}")
print(f"the Ethiopian year runs {1825030 - 1724221} days (276 years) ahead of the Coptic")
