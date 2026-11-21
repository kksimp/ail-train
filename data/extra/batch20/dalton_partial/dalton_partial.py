R = 8.314
vapour = {15: 1.71, 20: 2.34, 25: 3.17, 30: 4.25, 35: 5.63}
total = 101.3
for temp, ml in [(20, 245.0), (25, 250.0), (35, 262.0)]:
    pw = vapour.get(temp, 0.0)
    pgas = total - pw
    moles = pgas * 1000.0 * ml / 1000000.0 / (R * (float(temp) + 273.15))
    print(f"{ml} mL of hydrogen at {temp} C: water {pw} kPa, hydrogen {pgas:.2f} kPa, {moles * 1000.0:.3f} mmol")
air = [("N2", 0.7808), ("O2", 0.2095), ("Ar", 0.0093), ("CO2", 0.0004)]
for where, p in [("sea level", 101.3), ("Everest summit", 33.7)]:
    parts = ", ".join(f"{g[0]} {g[1] * p:.2f}" for g in air)
    print(f"{where} ({p} kPa): {parts} kPa")
