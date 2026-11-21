def load(f): return f[1] * f[2] // 100
def band(gl):
    if gl <= 10: return "Low"
    if gl < 20: return "Medium"
    return "High"
foods = [("watermelon, 120 g", 72, 6), ("white rice, 150 g", 73, 42), ("lentils, 150 g", 32, 18), ("baked potato, 150 g", 85, 30), ("apple, 120 g", 36, 15), ("cornflakes, 30 g", 81, 26), ("wholegrain bread, 60 g", 51, 28)]
counts = {}
for f in foods:
    gl = load(f); b = band(gl)
    counts[b] = counts.get(b, 0) + 1
    print(f"{f[0]:<23} GI {f[1]:>2}, {f[2]:>2} g carbs: GL {gl:>2} Load.{b}")
meal = [foods[1], foods[2], foods[4]]
total = 0
for f in meal: total = total + load(f)
print(f"rice, lentils and an apple: GL {total} (Load.{band(total)})")
for name in ["Low", "Medium", "High"]:
    print(f"{name}: {counts.get(name, 0)}")
