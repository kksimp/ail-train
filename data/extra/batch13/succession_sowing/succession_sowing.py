def date(n):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    left = n
    m = 0
    while left > days[m]:
        left -= days[m]
        m += 1
    return f"{months[m]} {left}"

def sowings(c, frost):
    out = []
    d = c[1]
    while d + c[2] <= frost:
        out.append(d)
        d += c[3]
    return out

frost = 288
crops = [("radish", 91, 28, 21), ("lettuce", 100, 55, 28), ("bean", 135, 60, 35), ("carrot", 105, 75, 42)]
print(f"first frost {date(frost)}")
for c in crops:
    days = sowings(c, frost)
    shown = ", ".join(date(d) for d in days)
    last_pick = days[-1] + c[2] + c[3]
    print(f"{c[0]:<8} {len(days)} sowings: {shown}")
    print(f"         harvest from {date(days[0] + c[2])} to about {date(min(last_pick, frost))}")
