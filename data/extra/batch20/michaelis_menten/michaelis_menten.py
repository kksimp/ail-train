def line_fit(xs, ys):
    n = float(len(xs))
    a = 0.0
    for x in xs:
        a = a + x
    mx = a / n
    a = 0.0
    for y in ys:
        a = a + y
    my = a / n
    sxy = 0.0
    sxx = 0.0
    for i in range(len(xs)):
        sxy += (xs[i] - mx) * (ys[i] - my)
        sxx += (xs[i] - mx) * (xs[i] - mx)
    slope = sxy / sxx
    return slope, my - slope * mx

def rate(vmax, km, s):
    return vmax * s / (km + s)

subs = [0.5, 1.0, 2.0, 4.0, 8.0, 16.0]
measured = [1.98, 3.36, 4.95, 6.71, 7.94, 8.92]
for i in range(len(subs)):
    print(f"[S] {subs[i]:>5.1f} mM: v {measured[i]:.2f} umol/min (model {rate(10.0, 2.0, subs[i]):.2f})")
inv_s = [1.0 / s for s in subs]
inv_v = [1.0 / v for v in measured]
slope, intercept = line_fit(inv_s, inv_v)
vmax = 1.0 / intercept
km = slope * vmax
print(f"Lineweaver-Burk: Vmax {vmax:.2f} umol/min, Km {km:.2f} mM")
inhibited = [rate(vmax, km * 3.0, 2.0), rate(vmax, km, 2.0)]
print(f"a competitive inhibitor tripling Km cuts v at 2 mM from {inhibited[1]:.2f} to {inhibited[0]:.2f}")
