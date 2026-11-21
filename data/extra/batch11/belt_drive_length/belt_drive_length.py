PI = 3.141592653589793
def belt_length(big, small, centre):
    gap = big - small
    return 2.0 * centre + PI * (big + small) / 2.0 + gap * gap / (4.0 * centre)
standard = [900, 1000, 1120, 1250, 1400, 1600]
for big, small, centre in [(200.0, 100.0, 350.0), (250.0, 80.0, 400.0), (160.0, 160.0, 300.0), (315.0, 90.0, 450.0)]:
    need = belt_length(big, small, centre)
    pick = next((b for b in standard if float(b) >= need), 0)
    driven = 1450.0 * small / big
    speed = PI * small / 1000.0 * 1450.0 / 60.0
    print(f"D {big} d {small} C {centre}: {need:>6.1f} mm -> belt {pick}, driven {driven:>6.1f} rpm, belt {speed:.2f} m/s")
