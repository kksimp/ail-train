def month_index(name):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months.index(name) + 1

def days_in(y, m):
    if m == 2:
        leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
        return 29 if leap else 28
    return 30 if m in [4, 6, 9, 11] else 31

def zone_minutes(z):
    named = {"GMT": 0, "UT": 0, "EST": -300, "EDT": -240, "PST": -480, "PDT": -420}
    if z in named:
        return named[z]
    sign = -1 if z.startswith("-") else 1
    return sign * (int(z[1:3]) * 60 + int(z[3:5]))

def to_utc(header):
    rest = header.split(", ")[1] if "," in header else header
    p = rest.split()
    d = int(p[0])
    m = month_index(p[1])
    y = int(p[2])
    hms = [int(x) for x in p[3].split(":")]
    minutes = hms[0] * 60 + hms[1] - zone_minutes(p[4])
    if minutes < 0:
        minutes += 1440
        d -= 1
        if d == 0:
            m -= 1
            if m == 0:
                m = 12
                y -= 1
            d = days_in(y, m)
    elif minutes >= 1440:
        minutes -= 1440
        d += 1
        if d > days_in(y, m):
            d = 1
            m += 1
            if m == 13:
                m = 1
                y += 1
    return f"{y}-{m:02}-{d:02}T{minutes // 60:02}:{minutes % 60:02}:{hms[2]:02}Z"

headers = ["Tue, 05 Mar 2024 14:03:00 +0100", "Wed, 31 Dec 2025 22:30:15 -0330", "1 Mar 2024 00:20:00 +0530", "Fri, 28 Feb 2025 23:59:59 PST", "Mon, 10 Jun 2024 08:00:00 GMT", "Sun, 01 Jan 2023 01:00:00 +1400"]
for h in headers:
    print(f"{h:<33} -> {to_utc(h)}")
