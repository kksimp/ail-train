def parsecs(mas): return 1000.0 / mas
stars = [("Proxima Centauri", 768.07, 0.03), ("Sirius", 379.21, 1.58), ("Vega", 130.23, 0.36), ("Betelgeuse", 5.95, 0.58), ("Deneb", 2.29, 0.32)]
for name, mas, err in sorted(stars, key=lambda s: -int(s[1] * 100.0)):
    d = parsecs(mas)
    ly = d * 3.2616
    near = parsecs(mas + err)
    far = parsecs(mas - err)
    pct = err / mas * 100.0
    print(f"{name:<16} {mas:>7.2f} mas: {d:>7.2f} pc = {ly:>7.1f} ly (range {near:.2f} to {far:.2f} pc, {pct:.2f}% error)")
print("over 10% error: " + ", ".join(s[0] for s in stars if s[2] / s[1] > 0.1))
