import math
stages = [("first", 400.0, 25.0, 300.0), ("second", 90.0, 6.0, 345.0), ("third", 12.0, 1.5, 450.0)]
def delta_v(full, empty, isp):
    return isp * 9.80665 * math.log(full / empty)
payload = 5.0
total = 0.0
for i, s in enumerate(stages):
    above = payload
    for j in range(i + 1, len(stages)):
        above += stages[j][1] + stages[j][2]
    full = s[1] + s[2] + above
    empty = s[2] + above
    dv = delta_v(full, empty, s[3])
    total += dv
    print(f"{s[0]:<6} stage: {full:>6.1f} t -> {empty:>6.1f} t, dv {dv:>7.1f} m/s")
verdict = "reaches orbit" if total >= 9400.0 else "falls short of orbit"
print(f"total {total:.1f} m/s: {verdict}")
single = delta_v(400.0 + 90.0 + 12.0 + 25.0 + 6.0 + 1.5 + payload, 25.0 + 6.0 + 1.5 + payload, 300.0)
print(f"one big stage with the same masses: {single:.1f} m/s")
