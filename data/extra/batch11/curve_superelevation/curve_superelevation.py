def friction(kmh):
    return 0.16 if kmh <= 50.0 else (0.14 if kmh <= 80.0 else (0.12 if kmh <= 100.0 else 0.1))
def min_radius(kmh, e):
    return kmh * kmh / (127.0 * (e + friction(kmh)))
e = 0.06
for v in [50.0, 70.0, 90.0, 110.0, 130.0]:
    r = min_radius(v, e)
    print(f"{v:>5.1f} km/h: f {friction(v)}, minimum radius {r:>6.1f} m")
for radius in [80.0, 250.0, 600.0]:
    speed = 30.0
    while speed + 10.0 <= 150.0 and min_radius(speed + 10.0, e) <= radius:
        speed += 10.0
    print(f"a {radius} m curve is safe up to {speed} km/h")
