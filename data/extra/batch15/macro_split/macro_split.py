def grams(total, m): return total * m[1] / m[2]
target = 2400.0
macros = [("protein", 0.3, 4.0), ("carbohydrate", 0.4, 4.0), ("fat", 0.3, 9.0)]
eaten = {"protein": 142.0, "carbohydrate": 265.0, "fat": 96.0}
energy = 0.0
for m in macros:
    g = grams(target, m)
    got = eaten[m[0]]
    energy += got * m[2]
    diff = got - g
    word = "over" if diff >= 0.0 else "under"
    print(f"{m[0]:<12} target {g:>5.1f} g, eaten {got:>5.1f} g, {abs(diff):.1f} g {word}")
pct = energy / target * 100.0
print(f"energy eaten {energy:.0f} kcal, {pct:.1f}% of target")
per_meal = grams(target, macros[0]) / 4.0
print(f"protein per meal over 4 meals: {per_meal:.1f} g")
