import math

def zone(lat, lon):
    if lat < -80.0 or lat >= 84.0:
        return None
    bands = "CDEFGHJKLMNPQRSTUVWX"
    bi = min(int(math.floor((lat + 80.0) / 8.0)), 19)
    band = bands[bi]
    z = int(math.floor((lon + 180.0) / 6.0)) + 1
    if band == 'V' and lon >= 3.0 and lon < 12.0:
        z = 32
    if band == 'X' and lon >= 0.0 and lon < 42.0:
        z = 31 if lon < 9.0 else 33 if lon < 21.0 else 35 if lon < 33.0 else 37
    return f"{z}{band}"

places = [("Bergen", 60.39, 5.32), ("Oslo", 59.91, 10.75), ("Longyearbyen", 78.22, 15.65), ("London", 51.51, -0.13), ("Nairobi", -1.29, 36.82), ("Quito", -0.18, -78.47), ("Auckland", -36.85, 174.76), ("South Pole", -90.0, 0.0), ("Alert", 82.5, -62.3)]
for name, lat, lon in places:
    z = zone(lat, lon)
    if z is not None:
        zn = int(z[:len(z) - 1])
        print(f"{name:<13} {z:<4} central meridian {zn * 6 - 183}")
    else:
        print(f"{name:<13} polar, use UPS")
