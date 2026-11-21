def det3(m):
    return m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])

def with_column(m, col, v):
    out = [row[:] for row in m]
    for r in range(3):
        out[r][col] = v[r]
    return out

def fit(xs, ys):
    s = [0.0] * 5
    t = [0.0] * 3
    for i in range(len(xs)):
        p = 1.0
        for k in range(5):
            s[k] += p
            if k < 3:
                t[k] += p * ys[i]
            p *= xs[i]
    m = [[s[0], s[1], s[2]], [s[1], s[2], s[3]], [s[2], s[3], s[4]]]
    d = det3(m)
    return [det3(with_column(m, 0, t)) / d, det3(with_column(m, 1, t)) / d, det3(with_column(m, 2, t)) / d]

times = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
heights = [1.9, 12.3, 20.2, 25.8, 28.6, 29.1, 27.2]
c = fit(times, heights)
print(f"h(t) = {c[0]:.3f} + {c[1]:.3f} t + {c[2]:.3f} t^2")
print(f"gravity estimate {-2.0 * c[2]:.2f} m/s^2, launch speed {c[1]:.2f} m/s")
sse = 0.0
for i in range(len(times)):
    t = times[i]
    pred = c[0] + c[1] * t + c[2] * t * t
    sse += (heights[i] - pred) * (heights[i] - pred)
    print(f"t {t:.1f}: measured {heights[i]:>5.1f}, fitted {pred:>6.2f}")
print(f"sum of squared errors {sse:.4f}")
peak = -c[1] / (2.0 * c[2])
print(f"highest at t = {peak:.3f} s")
