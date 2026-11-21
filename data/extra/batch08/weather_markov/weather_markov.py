names = ["sunny", "cloudy", "rainy"]; table = [[0.7, 0.2, 0.1], [0.3, 0.4, 0.3], [0.2, 0.4, 0.4]]
def step(d):
    out = [0.0, 0.0, 0.0]
    for f in range(3):
        for t in range(3): out[t] += d[f] * table[f][t]
    return out
d = [1.0, 0.0, 0.0]; rw = 0.0
for day in range(1, 8):
    d = step(d); rw += d[2]; print(f"day {day}: sunny {d[0]:.3f}, cloudy {d[1]:.3f}, rainy {d[2]:.3f}")
print(f"expected rainy days in the week: {rw:.2f}")
for n in range(60): d = step(d)
for k in range(3): print(f"long run {names[k]}: {d[k]:.3f}")
