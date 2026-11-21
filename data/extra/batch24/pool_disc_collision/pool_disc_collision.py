import math
ax = 0.0; ay = 0.0; avx = 3.0; avy = 0.0
bx = 5.0; by_ = 0.9
t = 0.0; dt = 0.001
while True:
    dx = bx - ax; dy = by_ - ay
    if dx * dx + dy * dy <= 4.0: break
    ax += avx * dt; ay += avy * dt; t += dt
dx = bx - ax; dy = by_ - ay
d = math.sqrt(dx * dx + dy * dy)
nx = dx / d; ny = dy / d
along = avx * nx + avy * ny
bvx = along * nx; bvy = along * ny
avx -= bvx; avy -= bvy
print(f"contact after {t:.3f} s with the cue ball at ({ax:.3f}, {ay:.3f})")
print(f"cue ball leaves at ({avx:.3f}, {avy:.3f}) m/s")
print(f"object ball leaves at ({bvx:.3f}, {bvy:.3f}) m/s")
ke = avx * avx + avy * avy + bvx * bvx + bvy * bvy
right_angle = abs(avx * bvx + avy * bvy) < 0.000001
print(f"speed squared before 9.0, after {ke:.6f}; paths at right angles: {'true' if right_angle else 'false'}")
