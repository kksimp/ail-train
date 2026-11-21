def ceil_div(a, b):
    return (a + b - 1) // b
for name, tv, ta in [("e-bike", 360, 150), ("drill", 180, 60), ("scooter", 480, 100), ("power bank", 36, 200)]:
    s = ceil_div(tv, 36)
    strings = ceil_div(ta, 30)
    cells = s * strings
    nominal = float(s) * 3.6
    full = float(s) * 4.2
    ah = float(strings) * 3.0
    wh = nominal * ah
    kg = float(cells * 48) / 1000.0
    print(f"{name:<10} {s}s{strings}p: {cells:>3} cells, {nominal:.1f} V ({full:.1f} V full), {ah:.1f} Ah, {int(wh)} Wh, {kg:.2f} kg")
