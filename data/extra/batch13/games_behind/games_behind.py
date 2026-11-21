clubs = [("Harbor", 71, 60), ("Summit", 75, 55), ("Prairie", 68, 64), ("Canyon", 74, 57), ("Delta", 59, 72)]

def trunc_div(a, b):
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b > 0) else -q

def games_behind(lead, c):
    return float((lead[1] - c[1]) + (c[2] - lead[2])) / 2.0

table = sorted(clubs, key=lambda c: trunc_div(-c[1] * 10000, c[1] + c[2]))
lead = table[0]
print("team       W   L   pct    GB")
for c in table:
    gb = games_behind(lead, c)
    shown = "-" if gb == 0.0 else f"{gb:.1f}"
    pct = f"{float(c[1]) / float(c[1] + c[2]):.3f}"[1:]
    print(f"{c[0]:<8} {c[1]:>3} {c[2]:>3}  {pct}  {shown:>4}")
last = table[-1]
print(f"{last[0]} trail by {games_behind(lead, last):.1f} with {162 - last[1] - last[2]} to play")
