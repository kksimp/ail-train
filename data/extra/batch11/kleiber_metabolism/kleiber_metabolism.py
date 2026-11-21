def daily_kcal(kg):
    return 70.0 * kg ** 0.75
for name, kg in [("mouse", 0.02), ("rat", 0.3), ("cat", 4.0), ("human", 70.0), ("horse", 500.0), ("elephant", 5000.0)]:
    day = daily_kcal(kg)
    per_kg = day / kg
    print(f"{name:<8} {kg:>7.2f} kg: {day:>9.1f} kcal a day, {per_kg:>6.1f} per kg")
ratio = daily_kcal(5000.0) / daily_kcal(0.02)
mass_ratio = 5000.0 / 0.02
print(f"an elephant weighs {mass_ratio:.1f} times a mouse but burns only {ratio:.1f} times as much")
