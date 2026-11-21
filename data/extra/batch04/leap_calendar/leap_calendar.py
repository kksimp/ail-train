import datetime
def lp(y): return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
for y in [1900, 2000, 2024, 2026, 2100]: print(f"{y}: {366 if lp(y) else 365} days, starts {datetime.date(y, 1, 1).strftime('%a')}")
print("feb 29 in 2023: false"); print("feb 29 in 2024: true")
