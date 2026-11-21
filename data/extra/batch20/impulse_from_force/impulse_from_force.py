def area_units(fs):
    total = 0
    for i in range(len(fs) - 1):
        total += fs[i] + fs[i + 1]
    return total

def impulse(fs):
    return float(area_units(fs)) * 0.0005

ball = 0.43
kicks = [("instep drive", [0, 120, 480, 950, 1300, 1420, 1250, 900, 450, 150, 0]), ("toe poke", [0, 600, 1700, 2100, 1500, 500, 0]), ("side foot pass", [0, 80, 210, 330, 400, 410, 380, 300, 190, 90, 30, 0])]
for name, fs in kicks:
    j = impulse(fs)
    ms = len(fs) - 1
    peak = max(fs)
    mean = j / (float(ms) / 1000.0)
    speed = j / ball
    print(f"{name:<15} J {j:.3f} N s over {ms} ms, peak {peak} N, mean {mean:.0f} N, ball {speed:.1f} m/s")
best = max(kicks, key=lambda k: impulse(k[1]))
print(f"fastest ball: {best[0]}")
