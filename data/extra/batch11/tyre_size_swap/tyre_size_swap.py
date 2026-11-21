def diameter(t):
    return 2.0 * float(t[0]) * float(t[1]) / 100.0 + float(t[2]) * 25.4
def label(t):
    return f"{t[0]}/{t[1]}R{t[2]}"
original = (205, 55, 16)
base = diameter(original)
print(f"original {label(original)}: {base:.1f} mm, {base * 3.141592653589793 / 1000.0:.3f} m per turn")
for t in [(225, 45, 17), (215, 55, 16), (225, 40, 18), (195, 65, 15), (235, 45, 18)]:
    d = diameter(t)
    diff = (d - base) / base * 100.0
    real = 100.0 * d / base
    ok = "fits" if abs(diff) <= 3.0 else "too different"
    print(f"{label(t):<9} {d:.1f} mm ({diff:>5.2f}%): at 100 on the dial you do {real:.1f} km/h, {ok}")
