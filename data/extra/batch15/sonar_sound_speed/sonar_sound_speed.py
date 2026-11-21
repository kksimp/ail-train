def speed(t, s, z):
    return 1449.2 + 4.6 * t - 0.055 * t * t + 0.00029 * t * t * t + (1.34 - 0.01 * t) * (s - 35.0) + 0.016 * z
layers = [(0.0, 50.0, 22.0, 36.0), (50.0, 200.0, 15.0, 35.5), (200.0, 800.0, 8.0, 35.0), (800.0, 1500.0, 4.0, 34.8)]
echo = 0.0
for top, bottom, temp, sal in layers:
    mid = (top + bottom) / 2.0
    c = speed(temp, sal, mid)
    echo += 2.0 * (bottom - top) / c
    print(f"{top:>6.0f} to {bottom:>6.0f} m: {temp:>4.1f} C, {c:.1f} m/s")
depth = layers[-1][1]
guessed = echo * 1500.0 / 2.0
print(f"echo returns after {echo:.4f} s")
print(f"at a fixed 1500 m/s that reads {guessed:.1f} m instead of {depth:.0f} m")
