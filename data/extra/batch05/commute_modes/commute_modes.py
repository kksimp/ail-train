M = [("bike", 15, 28, 0), ("bus", 240, 35, 820), ("car", 410, 19, 2300)]
for n, c, mi, co in M:
    t = c * 44; print(f"{n:<5} {t // 100:>3}.{t % 100:02} {mi * 44 / 60:>5.1f} h {co * 44 / 1000:>6.1f} kg")
print(f"cheapest {min(M, key=lambda m: m[1])[0]}, fastest {min(M, key=lambda m: m[2])[0]}, greenest {min(M, key=lambda m: m[3])[0]}")
