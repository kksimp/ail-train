def minutes(t):
    parts = t.split(":")
    return float(int(parts[0])) + float(int(parts[1])) / 60.0

climbs = [("Col du Pin", 8.4, 7.2, "27:40"), ("Mur de Brac", 1.2, 12.5, "5:55"), ("Alto Verde", 14.8, 6.1, "48:12"), ("Passo Nero", 21.0, 5.4, "69:00"), ("Hill Road", 3.5, 4.0, "9:05")]
best = ""
best_vam = 0.0
for name, km, grade, time in climbs:
    gain = km * grade * 10.0
    hours = minutes(time) / 60.0
    vam = gain / hours
    wkg = vam / ((2.0 + grade / 10.0) * 100.0)
    if vam > best_vam:
        best_vam = vam
        best = name
    print(f"{name:<11} {gain:>6.0f} m in {time:>5}  VAM {vam:>5.0f} m/h  about {wkg:.2f} W/kg")
print(f"fastest climbing: {best}")
