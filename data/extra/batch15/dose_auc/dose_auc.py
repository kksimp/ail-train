import math
times = [0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0]
conc = [0.0, 4.3, 6.9, 8.2, 7.0, 5.9, 4.1, 2.9, 1.4]
cmax = 0.0; tmax = 0.0; auc = 0.0
for i in range(len(times)):
    if conc[i] > cmax:
        cmax = conc[i]; tmax = times[i]
    if i > 0:
        auc += (conc[i] + conc[i - 1]) / 2.0 * (times[i] - times[i - 1])
print(f"Cmax {cmax:.1f} mg/L at Tmax {tmax:.1f} h")
print(f"AUC 0-12 h by trapezoids: {auc:.1f} mg h/L")
n = 3
sx = sy = sxx = sxy = 0.0
for i in range(len(times) - n, len(times)):
    y = math.log(conc[i])
    sx += times[i]; sy += y; sxx += times[i] * times[i]; sxy += times[i] * y
nf = float(n)
slope = (nf * sxy - sx * sy) / (nf * sxx - sx * sx)
ke = -slope
half = math.log(2.0) / ke
tail = conc[-1] / ke
print(f"ke {ke:.4f} per h, half-life {half:.2f} h")
print(f"AUC to infinity {auc + tail:.2f} mg h/L ({tail / (auc + tail) * 100.0:.1f}% extrapolated)")
