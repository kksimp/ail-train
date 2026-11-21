groups = [("none", [20.0, 22.0, 19.0, 24.0, 21.0]), ("compost", [25.0, 27.0, 24.0, 26.0, 28.0]), ("nitrate", [23.0, 30.0, 26.0, 29.0, 27.0])]

def total(xs):
    s = 0.0
    for x in xs:
        s += x
    return s

all_values = []
for _, ys in groups:
    all_values.extend(ys)
grand = total(all_values) / float(len(all_values))
ssb = 0.0
ssw = 0.0
for name, ys in groups:
    m = total(ys) / float(len(ys))
    ssb += float(len(ys)) * (m - grand) * (m - grand)
    for y in ys:
        ssw += (y - m) * (y - m)
    print(f"{name:<8} mean {m:.2f}")
dfb = len(groups) - 1
dfw = len(all_values) - len(groups)
f = (ssb / float(dfb)) / (ssw / float(dfw))
print(f"grand mean {grand:.3f}, between SS {ssb:.3f} (df {dfb}), within SS {ssw:.3f} (df {dfw})")
verdict = "differ" if f > 3.89 else "do not clearly differ"
print(f"F = {f:.3f}; critical 3.89 at 5%: the means {verdict}")
