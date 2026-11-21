def classify(rate):
    if rate > 9.8: return "Unstable"
    if rate > 6.0: return "Conditional"
    return "Stable"
heights = [0, 500, 1000, 1500, 2500, 3500, 5000]
temps = [24.0, 18.5, 14.6, 10.9, 4.2, 0.8, -9.5]
counts = {}
for i in range(1, len(heights)):
    dz = float(heights[i] - heights[i - 1]) / 1000.0
    rate = (temps[i - 1] - temps[i]) / dz
    c = classify(rate)
    counts[c] = counts.get(c, 0) + 1
    print(f"{heights[i - 1]:>4} to {heights[i]:>4} m: {temps[i - 1]:>5.1f} -> {temps[i]:>5.1f} C, lapse {rate:>5.2f} C/km, Stability.{c}")
overall = (temps[0] - temps[-1]) / 5.0
print(f"whole column {overall:.2f} C/km: Stability.{classify(overall)}")
for name, n in counts.items():
    print(f"{name}: {n} layers")
