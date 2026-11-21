trees = [("oak", 0.65, 60.0, 22.0), ("birch", 0.55, 25.0, 15.0), ("pine", 0.42, 40.0, 25.0), ("beech", 0.62, 45.0, 28.0), ("willow", 0.38, 30.0, 12.0)]
def biomass(t):
    x = t[1] * t[2] * t[2] * t[3]
    return 0.0673 * x ** 0.976
total_co2 = 0.0
for t in trees:
    mass = biomass(t)
    carbon = mass * 0.47
    co2 = carbon * 3.67
    total_co2 += co2
    print(f"{t[0]:<7} {t[2]} cm x {t[3]} m: {mass:>7.1f} kg wood, {carbon:>6.1f} kg C, {co2 / 1000.0:.2f} t CO2")
print(f"the five trees hold {total_co2 / 1000.0:.2f} t of CO2")
order = [t[0] for t in sorted(trees, key=lambda t: 0 - int(biomass(t)))]
print("heaviest first: " + ", ".join(order))
