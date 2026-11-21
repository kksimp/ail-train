for s, t in [(3.0, 20.0), (6.5, 20.0), (12.0, 5.0), (2.0, 30.0), (9.0, -2.0)]:
    v = 331.3 + 0.606 * t; k = s * v / 1000.0; print(f"{s:.1f} s at {t:.0f} C: sound {v:.1f} m/s, {k:.2f} km away{' - go inside' if k < 3.0 else ''}")
