import math
def days_from_civil(y, m, d):
    yy = y - 1 if m <= 2 else y
    era = yy // 400
    yoe = yy - era * 400
    mp = (m + 9) % 12
    doy = (153 * mp + 2) // 5 + d - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe - 719468
def gmst(y, m, d, ut):
    days = float(days_from_civil(y, m, d) - days_from_civil(2000, 1, 1)) - 0.5 + ut / 24.0
    h = 18.697374558 + 24.06570982441908 * days
    return h - 24.0 * float(math.floor(h / 24.0))
def hms(hours):
    secs = int(hours * 3600.0)
    return f"{secs // 3600:02}:{secs // 60 % 60:02}:{secs % 60:02}"
for y, m, d, ut in [(2000, 1, 1, 12.0), (2024, 3, 20, 0.0), (2025, 6, 21, 22.5), (2026, 11, 21, 6.0)]:
    g = gmst(y, m, d, ut)
    print(f"{y}-{m:02}-{d:02} {hms(ut)} UT: GMST {hms(g)}")
g = gmst(2026, 11, 21, 6.0)
for name, lon in [("Greenwich", 0.0), ("Sydney", 151.21), ("Chicago", -87.63)]:
    local = g + lon / 15.0
    fixed = local - 24.0 * float(math.floor(local / 24.0))
    print(f"  local sidereal time at {name}: {hms(fixed)}")
