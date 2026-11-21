base = 0.1
acids = [("hydrochloric", 1, 0.1, 25.0), ("sulfuric", 2, 0.05, 20.0), ("citric", 3, 0.02, 25.0), ("acetic", 1, 0.85, 10.0)]
for name, p, molar, ml in acids:
    v = molar * ml * float(p) / base
    burette = " (refill the 50 mL burette)" if v > 50.0 else ""
    print(f"{ml} mL of {molar} M {name}: {v:.2f} mL of 0.1 M base{burette}")
titres = [22.4, 22.6, 22.5]
total = 0.0
for t in titres:
    total = total + t
mean = total / float(len(titres))
unknown = base * mean / (2.0 * 25.0)
print(f"unknown sulfuric acid, 25 mL, mean titre {mean:.2f} mL: {unknown:.4f} M")
