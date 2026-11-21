years = [(1960, 4210, 5900, 520), (1980, 4480, 7650, 790), (2000, 3720, 9480, 1150), (2020, 2960, 10120, 1890), (2040, 2610, 9300, 2950)]

def ratio(c, n):
    return n / c[2] * 100.0

print("year  youth   old  total  workers per older person")
for c in years:
    y = ratio(c, c[1])
    o = ratio(c, c[3])
    t = y + o
    support = c[2] / c[3]
    tag = "  window" if t < 50.0 else ""
    print(f"{c[0]}  {y:>5.1f} {o:>5.1f}  {t:>5.1f}  {support:>5.1f}{tag}")
first = 0
for c in years:
    if first == 0 and ratio(c, c[1]) + ratio(c, c[3]) < 50.0:
        first = c[0]
print(f"first census inside the window: {first}")
