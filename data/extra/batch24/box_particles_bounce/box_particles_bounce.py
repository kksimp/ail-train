w = 10.0; h = 6.0
ps = [[1.0, 1.0, 4.3, 2.7], [5.0, 3.0, -3.1, 1.9], [8.0, 5.0, 1.7, -4.4], [2.0, 4.0, -2.6, -2.2], [6.0, 1.5, 5.2, 0.9]]
hits = [0, 0, 0, 0]
dt = 0.05
for step in range(200):
    for p in ps:
        p[0] += p[2] * dt
        p[1] += p[3] * dt
        if p[0] < 0.0:
            p[0] = -p[0]; p[2] = -p[2]; hits[0] += 1
        elif p[0] > w:
            p[0] = 2.0 * w - p[0]; p[2] = -p[2]; hits[1] += 1
        if p[1] < 0.0:
            p[1] = -p[1]; p[3] = -p[3]; hits[2] += 1
        elif p[1] > h:
            p[1] = 2.0 * h - p[1]; p[3] = -p[3]; hits[3] += 1
for i, p in enumerate(ps):
    print(f"particle {i + 1}: at ({p[0]:.2f}, {p[1]:.2f})")
print(f"wall hits in 10 s: left {hits[0]}, right {hits[1]}, floor {hits[2]}, ceiling {hits[3]}")
