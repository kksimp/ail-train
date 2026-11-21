import math

def hundredths(t):
    mins = 0
    rest = t
    if ":" in t:
        parts = t.split(":")
        mins = int(parts[0])
        rest = parts[1]
    secs = rest.split(".")
    return mins * 6000 + int(secs[0]) * 100 + int(secs[1])

def points(base, swim):
    r = hundredths(base) / hundredths(swim)
    return int(math.floor(1000.0 * r * r * r))

bases = {"50 free": "20.91", "100 back": "51.60", "200 fly": "1:50.34", "400 IM": "4:02.50"}
swims = [("Nora", "50 free", "23.45"), ("Teo", "100 back", "55.10"), ("Ines", "200 fly", "2:01.88"), ("Mats", "400 IM", "4:21.07"), ("Pia", "50 free", "24.02"), ("Ravi", "200 fly", "1:58.40"), ("Sol", "100 back", "1:02.30")]
ranked = sorted(swims, key=lambda s: -points(bases[s[1]], s[2]))
for name, event, time in ranked:
    print(f"{name:<5} {event:<9} {time:>8}  {points(bases[event], time):>4} points")
print(f"a swim 1% over the base scores {points('1:00.00', '1:00.60')}")
