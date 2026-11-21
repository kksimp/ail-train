team = [("Adeyemi", 612, 470, 228, 41, 150), ("Brandt", 480, 410, 170, 92, 60), ("Castro", 395, 300, 150, 10, 140), ("Dube", 260, 240, 95, 48, 30)]
def ts(s):
    return float(s[1]) / (2.0 * (float(s[2]) + 0.44 * float(s[5])))
def efg(s):
    return (float(s[3]) + 0.5 * float(s[4])) / float(s[2])
ranked = sorted(team, key=lambda s: 0 - int(ts(s) * 10000.0))
for s in ranked:
    fg = float(s[3]) / float(s[2]) * 100.0
    print(f"{s[0]:<9} FG {fg:.1f}%, eFG {efg(s) * 100.0:.1f}%, TS {ts(s) * 100.0:.1f}%")
pts = sum(s[1] for s in team)
print(f"team points {pts}")
