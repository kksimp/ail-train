NAMES = ["red", "orange", "yellow", "chartreuse", "green", "spring green", "cyan", "azure", "blue", "violet", "magenta", "rose"]
SCHEMES = [("Complementary", [0, 180]), ("Triadic", [0, 120, 240]), ("Analogous", [330, 0, 30]), ("SplitComplementary", [0, 150, 210])]

def hue_name(h):
    return NAMES[(h + 15) % 360 // 30]

for base in [10, 200, 275]:
    print(f"base {base} ({hue_name(base)})")
    for name, offs in SCHEMES:
        hues = [(base + o) % 360 for o in offs]
        named = ", ".join(f"{h} {hue_name(h)}" for h in hues)
        print(f"  {name:<18} {named}")
