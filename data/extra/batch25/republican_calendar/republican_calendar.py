def day_number(y, m, d):
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045

def roman(n):
    vals = [10, 9, 5, 4, 1]
    syms = ["X", "IX", "V", "IV", "I"]
    out = []
    x = n
    for i in range(len(vals)):
        while x >= vals[i]:
            out.append(syms[i])
            x -= vals[i]
    return "".join(out)

def republican(y, m, d):
    months = ["Vendémiaire", "Brumaire", "Frimaire", "Nivôse", "Pluviôse", "Ventôse", "Germinal", "Floréal", "Prairial", "Messidor", "Thermidor", "Fructidor"]
    left = day_number(y, m, d) - day_number(1792, 9, 22)
    if left < 0 or day_number(y, m, d) >= day_number(1806, 1, 1):
        return None
    year = 1
    while True:
        length = 366 if year in (3, 7, 11) else 365
        if left < length:
            break
        left -= length
        year += 1
    if left >= 360:
        return f"jour complémentaire {left - 359}, year {roman(year)}"
    return f"{left % 30 + 1} {months[left // 30]} year {roman(year)}"

dates = [(1792, 9, 22), (1793, 9, 21), (1794, 7, 27), (1795, 10, 5), (1799, 11, 9), (1804, 12, 2), (1805, 12, 31), (1806, 1, 1), (1789, 7, 14)]
for y, m, d in dates:
    shown = f"{y}-{m:02}-{d:02}"
    r = republican(y, m, d)
    if r is not None:
        print(f"{shown}: {r}")
    else:
        print(f"{shown}: outside the Republican calendar")
