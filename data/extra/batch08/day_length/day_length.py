import math
def hd(lat, day):
    pi = 3.141592653589793
    dec = 23.44 * pi / 180.0 * math.sin(2.0 * pi * (284 + day) / 365.0); phi = lat * pi / 180.0
    c = -math.tan(phi) * math.tan(dec); c = min(1.0, max(-1.0, c))
    return 2.0 * math.atan2(math.sqrt(1.0 - c * c), c) * 180.0 / pi / 15.0
print("place          Mar 20  Jun 21  Dec 21")
for n, lat in [("Quito", -0.2), ("Cape Town", -33.9), ("Madrid", 40.4), ("London", 51.5), ("Reykjavik", 64.1), ("Longyearbyen", 78.2)]:
    print(f"{n:<13} {hd(lat, 79):>6.1f}h {hd(lat, 172):>6.1f}h {hd(lat, 355):>6.1f}h")
