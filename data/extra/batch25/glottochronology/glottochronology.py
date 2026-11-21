import math

pairs = [("English", "German", 59), ("English", "Dutch", 63), ("German", "Dutch", 81), ("Spanish", "Italian", 77), ("Spanish", "Portuguese", 85), ("English", "Spanish", 27), ("Swedish", "Danish", 88)]

def split_years(shared):
    c = shared / 100.0
    r = 0.86
    return math.log(c) / (2.0 * math.log(r)) * 1000.0

for a, b, shared in sorted(pairs, key=lambda p: -p[2]):
    t = split_years(shared)
    label = f"{a}-{b}"
    print(f"{label:<19} {shared:>3}% shared, split about {t:>5.0f} years ago")
r = 0.86
kept = r * r * 100.0
print(f"after 1000 years apart two languages still share {kept:.1f}%")
