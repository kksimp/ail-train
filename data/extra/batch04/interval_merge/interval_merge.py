R = sorted([(13, 14), (9, 10), (15, 17), (9, 11), (16, 18), (10, 12)]); m = []
for a, b in R:
    if m and a <= m[-1][1]: m[-1] = (m[-1][0], max(b, m[-1][1]))
    else: m.append((a, b))
print("busy: " + ", ".join(f"{a}-{b}" for a, b in m)); t = 9
for a, b in m:
    if a > t: print(f"free {t}-{a}")
    t = b
if t < 18: print(f"free {t}-18")
