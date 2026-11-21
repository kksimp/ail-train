def ideal(use, hot, cold):
    th = hot + 273.15
    tc = cold + 273.15
    if use == "Engine": return 1.0 - tc / th
    if use == "Fridge": return tc / (th - tc)
    return th / (th - tc)
ms = [("steam plant", "Engine", 550.0, 30.0), ("car engine", "Engine", 900.0, 90.0), ("kitchen fridge", "Fridge", 35.0, -2.0), ("freezer", "Fridge", 35.0, -25.0), ("floor heating", "HeatPump", 35.0, -5.0), ("radiators", "HeatPump", 55.0, -5.0)]
for name, use, hot, cold in ms:
    i = ideal(use, hot, cold)
    real = i * 0.5
    if use == "Engine":
        shown = f"efficiency {i * 100.0:.1f}%, real about {real * 100.0:.1f}%"
    else:
        shown = f"COP {i:.2f}, real about {real:.2f}"
    print(f"{name:<14} {hot:>5.0f} / {cold:>4.0f} C: {shown}")
