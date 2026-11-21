for n, mah, dr in [("doorbell", 6000, 4.5), ("headphones", 800, 35.0), ("trail camera", 12000, 18.0), ("smoke alarm", 1200, 0.02), ("torch", 2600, 450.0)]:
    h = mah * 0.85 / dr; w = int(h); print(f"{n:<12} {mah:>5} mAh at {dr:>6.2f} mA: {h:>9.1f} h ({w // 24} d {w % 24} h)")
