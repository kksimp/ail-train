import math
PI = 3.141592653589793
def rad(deg):
    return deg * PI / 180.0
course = 90.0
tas = 120.0
leg = 300.0
for from_deg, speed in [(45.0, 20.0), (135.0, 25.0), (200.0, 15.0), (300.0, 30.0), (10.0, 40.0)]:
    a = rad(from_deg - course)
    cross = speed * math.sin(a)
    head = speed * math.cos(a)
    x = cross / tas
    wca = math.atan2(x, math.sqrt(1.0 - x * x))
    ground = tas * math.cos(wca) - head
    heading = course + wca * 180.0 / PI
    minutes = leg / ground * 60.0
    print(f"wind {from_deg:>5.1f}/{speed}: heading {heading:>5.1f}, ground speed {ground:>5.1f} kt, {minutes:>5.1f} min for {leg} nm")
