for n, m in [("Amsterdam", 0), ("Denver", 1609), ("Cusco", 3399), ("La Paz", 3640), ("Everest base", 5364)]:
    b = 100.0 - m / 300.0; print(f"{n:<12} {m:>4} m: boils at {b:.1f} C, pasta +{(100.0 - b) * 0.5:.1f} min")
