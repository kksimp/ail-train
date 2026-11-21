def band(b):
    if b < 18.5: return "under"
    if b < 25.0: return "healthy"
    if b < 30.0: return "over"
    return "obese"
for n, h, w in [("Ola", 182, 77.5), ("Pia", 160, 45.0), ("Quin", 175, 92.3), ("Ravi", 168, 70.0), ("Sol", 190, 110.8)]:
    m = h / 100.0; b = w / (m * m)
    print(f"{n:<5} {b:5.1f} {band(b):<8} healthy {18.5 * m * m:.1f}-{25.0 * m * m:.1f} kg")
