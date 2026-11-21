a = 38; rs = 58; t = 220 - a; rv = t - rs; L = [rs + rv * p // 100 for p in [50, 60, 70, 80, 90]]
for i in range(4): print(f"zone {i + 1}: {L[i]}-{L[i + 1] - 1} bpm")
M = [0] * 6
for r in [96, 110, 121, 128, 135, 141, 150, 158, 163, 155, 149, 138, 126, 112]:
    z = 0
    for i in range(5):
        if r >= L[i]: z = i + 1
    M[z] += 1
for z in range(6):
    if M[z] > 0: print(f"{'below zone 1' if z == 0 else 'zone 5' if z == 5 else 'zone ' + str(z)}: {M[z]} min")
