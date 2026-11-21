pk = dict([("car", 0.17), ("bus", 0.10), ("train", 0.035), ("bike", 0.0), ("plane", 0.25)])
tot = 0.0
for m, km, n in [("car", 24.0, 10), ("train", 60.0, 2), ("bus", 8.0, 6), ("plane", 900.0, 1), ("bike", 5.0, 8)]:
    kg = km * n * pk[m]; tot += kg; print(f"{m:<6} {n:>2} x {km:>5.1f} km: {kg:>6.1f} kg")
print(f"month total: {tot:.1f} kg")
print(f"car commute by train instead saves {240.0 * (pk['car'] - pk['train']):.1f} kg")
