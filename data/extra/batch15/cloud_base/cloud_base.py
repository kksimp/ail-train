def base_agl(r): return 125.0 * (r[2] - r[3])
def freezing_level(r): return float(r[1]) + r[2] / 0.0065
reports = [("Coastal", 5, 18.0, 16.0), ("Valley", 120, 24.0, 12.0), ("Plateau", 900, 15.0, 2.0), ("Hill strip", 450, 9.0, 8.0)]
for r in reports:
    agl = base_agl(r)
    amsl = agl + float(r[1])
    feet = agl * 3.28084
    fz = freezing_level(r)
    icing = ", base above freezing level" if amsl > fz else ""
    print(f"{r[0]:<10} spread {r[2] - r[3]:>4.1f} C: base {agl:>5.0f} m ({feet:>5.0f} ft) above ground, {amsl:>5.0f} m above sea{icing}")
    print(f"           freezing level {fz:.0f} m")
low = [r[0] for r in reports if base_agl(r) < 300.0]
print("low cloud (under 300 m) at: " + ", ".join(low))
