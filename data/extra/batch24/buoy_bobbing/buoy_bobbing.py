def accel(depth, v):
    g = 9.8
    return g * (depth - 0.6) / 0.6 * -1.0 - 0.8 * v
depth = 0.2; v = 0.0; dt = 0.01; deepest = depth
for step in range(1, 601):
    v += accel(depth, v) * dt
    depth += v * dt
    deepest = max(deepest, depth)
    if step % 100 == 0:
        print(f"t {step // 100} s: depth {depth:.3f} m")
print(f"deepest {deepest:.3f} m, settling toward 0.600 m")
