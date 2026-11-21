lines = [("ceramic mugs", 1200, 1.85, 480.0, 0.06), ("steel pans", 300, 9.4, 690.0, 0.035), ("cotton towels", 800, 3.1, 260.0, 0.12)]
freight = 1450.0; insurance = 180.0
total_kg = 0.0
for l in lines: total_kg = total_kg + l[3]
total_value = 0.0
for l in lines: total_value = total_value + float(l[1]) * l[2]
grand = 0.0
for name, units, price, kg, rate in lines:
    value = float(units) * price
    f = freight * kg / total_kg
    ins = insurance * value / total_value
    cif = value + f + ins
    duty = cif * rate
    landed = cif + duty
    grand += landed
    unit = landed / float(units)
    print(f"{name:<13} goods {value:>7.2f} + freight {f:>6.2f} + insurance {ins:>5.2f} + duty {duty:>6.2f} = {landed:>8.2f}, {unit:.3f} a unit (+{(unit / price - 1.0) * 100.0:.1f}%)")
print(f"shipment landed cost {grand:.2f} for goods worth {total_value:.2f}")
