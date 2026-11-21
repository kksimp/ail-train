import math
def civil(z0):
    z = z0 + 719468
    era = z // 146097
    doe = z - era * 146097
    yoe = (doe - doe // 1460 + doe // 36524 - doe // 146096) // 365
    doy = doe - (365 * yoe + yoe // 4 - yoe // 100)
    mp = (5 * doy + 2) // 153
    d = doy - (153 * mp + 2) // 5 + 1
    m = mp + 3 if mp < 10 else mp - 9
    y = yoe + era * 400 + (1 if m <= 2 else 0)
    return [y, m, d]
synodic = 223.0 * 29.530589
draconic = 242.0 * 27.212221
anomalistic = 239.0 * 27.554550
print(f"223 synodic {synodic:.3f} d, 242 draconic {draconic:.3f} d, 239 anomalistic {anomalistic:.3f} d")
start = 17399.0 + 18.42 / 24.0
for k in range(5):
    t = start + float(k) * synodic
    day = int(math.floor(t))
    hour = (t - float(math.floor(t))) * 24.0
    ymd = civil(day)
    west = k * 120 % 360
    print(f"eclipse {k}: {ymd[0]}-{ymd[1]:02}-{ymd[2]:02} about {hour:.1f} h UT, shifted {west} deg west")
