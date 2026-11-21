gs = [("Margaret", "Hughes", "Maggie", "Northwind"), ("Tomasz", "Nowak", None, "Fabrikam"), ("Ines", "Duarte", "Ini", None)]
def center(s, w):
    pad = w - len(s); left = pad // 2
    return " " * left + s + " " * (pad - left)
b = "+" + "-" * 18 + "+"
for f, l, n, c in gs:
    print(b)
    for x in [(n or f).upper(), f"{f} {l}", c or "Guest"]: print(f"|{center(x, 18)}|")
print(b)
print(f"{sum(1 for g in gs if g[3] is None)} guests without a company")
