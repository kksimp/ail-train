stars = [("Sun", 1.0, 5772.0), ("Sirius A", 1.711, 9940.0), ("Rigel", 78.9, 12100.0), ("Betelgeuse", 764.0, 3600.0), ("Proxima", 0.154, 3042.0), ("Arcturus", 25.4, 4286.0)]
def colour(peak_nm):
    return "blue-white" if peak_nm < 400.0 else ("white" if peak_nm < 500.0 else ("yellow" if peak_nm < 600.0 else ("orange" if peak_nm < 750.0 else "red")))
def luminosity(s):
    t = s[2] / 5772.0
    return s[1] * s[1] * t * t * t * t
for s in stars:
    peak = 2897772.0 / s[2]
    print(f"{s[0]:<10} R {s[1]:>6.3f} T {s[2]:>7.1f} K: L {luminosity(s):>11.3f} Lsun, peak {peak:>4.1f} nm ({colour(peak)})")
brightest = max(stars, key=lambda st: int(luminosity(st)))
print(f"most luminous: {brightest[0]}")
