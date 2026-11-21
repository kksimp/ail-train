def parse(s):
    parts = s.split(":")
    if len(parts) != 2 or parts[0] != "1":
        return None
    try:
        return int(parts[1])
    except ValueError:
        return None

print("scale        1 cm      4 cm walk  1 km on map  1 cm2")
for text in ["1:10000", "1:25000", "1:50000", "1:63360", "1:250000", "1:1000000", "1/50000"]:
    n = parse(text)
    if n is not None:
        one_cm = n // 100
        walk = 4.0 * n / 100000.0
        km = 100000.0 / n
        ha = float(n) * float(n) / 100000000.0
        print(f"{text:<10} {one_cm:>7} m  {walk:>8.2f} km  {km:>8.3f} cm  {ha:>8.2f} ha")
    else:
        print(f"{text:<10} bad scale {text}")
