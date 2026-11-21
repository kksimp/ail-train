lines = [("Hale", 520.0, 350.0, 4200.0, 32.0, 9.0), ("Moreno", 480.0, 290.0, 3300.0, 18.0, 14.0), ("Quist", 300.0, 160.0, 1900.0, 8.0, 15.0), ("Perfect day", 20.0, 18.0, 300.0, 4.0, 0.0)]
def clamp(x):
    return 0.0 if x < 0.0 else (2.375 if x > 2.375 else x)
def rating(l):
    a = clamp((l[2] / l[1] - 0.3) * 5.0)
    b = clamp((l[3] / l[1] - 3.0) * 0.25)
    c = clamp(l[4] / l[1] * 20.0)
    d = clamp(2.375 - l[5] / l[1] * 25.0)
    return (a + b + c + d) / 6.0 * 100.0
for l in lines:
    pct = l[2] / l[1] * 100.0
    print(f"{l[0]:<11} {pct:>5.1f}% complete, {l[3] / l[1]:.3f} yd/att: rating {rating(l):.1f}")
best = max(lines, key=lambda x: int(rating(x) * 10.0))
print(f"best: {best[0]}")
