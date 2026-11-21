PI = 3.141592653589793
SIGMA = 0.0000000567

def cool(emiss, minutes):
    r = 0.05
    area = 4.0 * PI * r * r
    mass = 7850.0 * 4.0 / 3.0 * PI * r * r * r
    c = 490.0
    walls = 300.0
    t = 1000.0
    out = [t]
    for m in range(minutes):
        for s in range(6):
            t4 = t * t * t * t
            w4 = walls * walls * walls * walls
            t -= emiss * SIGMA * area * (t4 - w4) / (mass * c) * 10.0
        out.append(t)
    return out

dark = cool(0.95, 60)
shiny = cool(0.1, 60)
for m in [0, 5, 10, 20, 40, 60]:
    print(f"{m:>2} min: dark {dark[m]:>6.1f} K, polished {shiny[m]:>6.1f} K")
below = [i for i in range(len(dark)) if dark[i] < 600.0]
first = below[0] if below else -1
print(f"the dark ball falls below 600 K after {first} minutes")
