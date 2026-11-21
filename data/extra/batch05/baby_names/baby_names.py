Y = [(2022, {"Ava": 410, "Leo": 395, "Mia": 380, "Kai": 210, "Zoe": 300}), (2023, {"Ava": 400, "Leo": 420, "Mia": 350, "Kai": 290, "Ivy": 240}), (2024, {"Leo": 430, "Ava": 380, "Kai": 360, "Mia": 330, "Ivy": 310})]
for y, c in Y: print(f"{y}: " + ", ".join(sorted(c, key=lambda n: (-c[n], n))[:3]))
f = Y[0][1]; l = Y[-1][1]; cm = sorted(n for n in f if n in l); cl = max(cm, key=lambda n: (l[n] - f[n], n))
print(f"biggest climber: {cl} (+{l[cl] - f[cl]})"); print("every year: " + ", ".join(n for n in cm if all(n in y[1] for y in Y)))
