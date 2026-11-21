D = [600, 610, 619, 622, 640, 649, 660, 663, 666, 690, 700, 710]; F = []; sq = t = 0
for i in range(1, len(D)):
    g = D[i] - D[i - 1]; t += g; sq += g * g; n = " long" if g > 15 else " bunched" if g < 4 else ""
    if n: F.append(str(D[i]))
    print(f"{D[i - 1] // 60:02}:{D[i - 1] % 60:02} -> {D[i] // 60:02}:{D[i] % 60:02} gap {g}{n}")
print(f"average wait {sq / (2.0 * t):.2f} min (5.00 if regular); flagged arrivals at minute {', '.join(F)}")
