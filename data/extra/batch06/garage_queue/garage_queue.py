F = [0, 0]; N = ["Raf", "Sia"]
c = lambda h: f"{8 + h // 60:02}:{h % 60:02}"
for n, m in [("brakes", 90), ("service", 60), ("clutch", 240), ("tyres", 30), ("exhaust", 120), ("MOT", 45), ("battery", 20)]:
    k = 0 if F[0] <= F[1] else 1; s = F[k]; F[k] = s + m; print(f"{n:<8} {N[k]} {c(s)}-{c(F[k])}")
for k in range(2): print(f"{N[k]} done at {c(F[k])}")
