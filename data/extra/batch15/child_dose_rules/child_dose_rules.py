def child_dose(rule, adult, kg, months):
    if rule == "Clark": return adult * kg * 2.2046 / 150.0
    if rule == "Young": return adult * float(months // 12) / float(months // 12 + 12)
    return adult * float(months) / 150.0
adult = 500.0
for name, kg, months in [("Mia", 9.5, 10), ("Leo", 14.0, 30), ("Ava", 21.0, 72), ("Sam", 32.0, 120)]:
    parts = []
    lowest = adult
    for rule in ["Clark", "Young", "Fried"]:
        if rule == "Fried" and months >= 24: continue
        if rule == "Young" and months < 24: continue
        d = child_dose(rule, adult, kg, months)
        if d < lowest: lowest = d
        parts.append(f"{rule} {d:.0f} mg")
    print(f"{name:<4} {kg:>4.1f} kg, {months:>3} months: {', '.join(parts)}; give at most {lowest:.0f} mg")
