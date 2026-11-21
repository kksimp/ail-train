for n, k, x in [("pen spring", 300.0, 0.004), ("door closer", 900.0, 0.08), ("car suspension", 25000.0, 0.05), ("trampoline", 5000.0, 0.4)]:
    print(f"{n:<15} k {k:>7.0f} N/m, {x:>5.3f} m: force {k * x:>7.1f} N, energy {0.5 * k * x * x:>8.3f} J")
for x in [0.02, 0.05, 0.1]: print(f"toy launcher at {x:.2f} m: {x * (200.0 / 0.05) ** 0.5:.2f} m/s")
