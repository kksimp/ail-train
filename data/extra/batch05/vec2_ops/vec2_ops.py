import math
dt = 0.1; px = py_ = 0.0; vx = 6.0; vy = 8.0; st = 0
while True:
    vy += -9.8 * dt; vx += 0.0 * dt; px += vx * dt; py_ += vy * dt; st += 1
    if st % 4 == 0: print(f"t={st * dt:.1f} x={px:.2f} y={py_:.2f}")
    if py_ < 0: break
print(f"landed after {st} steps at x={px:.2f}, distance {math.sqrt(px * px + py_ * py_):.2f}, back {-px:.2f}")
print("check length 5.0")
