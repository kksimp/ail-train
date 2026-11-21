import math

def letter(base, i):
    return chr(base + i)

def locator(lat, lon):
    x = lon + 180.0
    y = lat + 90.0
    fx = math.floor(x / 20.0)
    fy = math.floor(y / 10.0)
    rx = x - fx * 20.0
    ry = y - fy * 10.0
    sx = math.floor(rx / 2.0)
    sy = math.floor(ry)
    ux = math.floor((rx - sx * 2.0) * 12.0)
    uy = math.floor((ry - sy) * 24.0)
    return f"{letter(65, fx)}{letter(65, fy)}{sx}{sy}{letter(97, ux)}{letter(97, uy)}"

def centre(loc):
    lon = float(ord(loc[0]) - 65) * 20.0 + float(ord(loc[2]) - 48) * 2.0 + (float(ord(loc[4]) - 97) + 0.5) / 12.0 - 180.0
    lat = float(ord(loc[1]) - 65) * 10.0 + float(ord(loc[3]) - 48) + (float(ord(loc[5]) - 97) + 0.5) / 24.0 - 90.0
    return [lat, lon]

places = [("London", 51.5074, -0.1278), ("Tokyo", 35.6762, 139.6503), ("New York", 40.7128, -74.006), ("Sydney", -33.8688, 151.2093), ("Cape Town", -33.9249, 18.4241), ("Reykjavik", 64.1466, -21.9426)]
for name, lat, lon in places:
    loc = locator(lat, lon)
    c = centre(loc)
    print(f"{name:<10} {lat:>8.4f} {lon:>9.4f} -> {loc}, centre {c[0]:.3f} {c[1]:.3f}")
