table = {
    "chlorine": [(34.969, 75.76), (36.966, 24.24)],
    "magnesium": [(23.985, 78.99), (24.986, 10.0), (25.983, 11.01)],
    "copper": [(62.93, 69.15), (64.928, 30.85)],
    "silicon": [(27.977, 92.23), (28.976, 4.68), (29.974, 3.09)],
}
def average(isos):
    t = 0.0
    for m, p in isos:
        t = t + m * p / 100.0
    return t
for name, isos in table.items():
    print(f"{name:<9} {len(isos)} isotopes: {average(isos):.3f}")
avg = 10.811
m1 = 10.013
m2 = 11.009
x = (avg - m2) / (m1 - m2) * 100.0
print(f"boron at {avg} from {m1} and {m2}: {x:.1f}% boron-10, {100.0 - x:.1f}% boron-11")
