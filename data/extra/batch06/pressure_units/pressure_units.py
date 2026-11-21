for n, v, u in [("front left", 34.0, "psi"), ("front right", 2.35, "bar"), ("rear left", 205.0, "kPa"), ("rear right", 31.5, "psi")]:
    b = v / 14.5038 if u == "psi" else v / 100.0 if u == "kPa" else v
    print(f"{n:<11} {b:.2f} bar {b * 14.5038:.1f} psi {b * 100.0:.0f} kPa{' LOW' if b < 2.4 * 0.9 else ''}")
