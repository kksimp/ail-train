def minutes(t):
    p = t.split(":")
    if len(p) != 2: return None
    try: h = int(p[0]); m = int(p[1])
    except ValueError: return None
    if h > 23 or m > 59: return None
    return h * 60 + m
def span(t):
    h = t.split("-")
    if len(h) != 2: return None
    a = minutes(h[0]); b = minutes(h[1])
    if a is None or b is None: return None
    return (a, b)
now = minutes("12:45"); op = 0
for n, hrs in [("bakery", "07:00-13:30"), ("library", "10:00-18:00"), ("barber", "9am-5pm"), ("pharmacy", "08:30-21:15"), ("cafe", "08:00-25:00")]:
    s = span(hrs)
    if s:
        st = "open" if s[0] <= now < s[1] else "closed"
        if st == "open": op += 1
        print(f"{n:<9} {hrs}: {st}, {s[1] - s[0]} min a day")
    else: print(f"{n:<9} {hrs}: hours unknown")
print(f"{op} shops open at 12:45")
