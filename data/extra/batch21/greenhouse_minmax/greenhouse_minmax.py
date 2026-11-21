days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
lows = [3, 1, 5, 2, 0, 4, 6, 8, 7, 2, 1, 3, 5, 6]
highs = [18, 22, 27, 24, 19, 28, 31, 26, 23, 17, 21, 29, 25, 24]
heater, vent = [], []
widest = 0
for i in range(len(lows)):
    name = f"{days[i % 7]} {i + 1}"
    if lows[i] <= 2:
        heater.append(name)
    if highs[i] >= 27:
        vent.append(name)
    if highs[i] - lows[i] > highs[widest] - lows[widest]:
        widest = i
print(f"heater nights ({len(heater)}): {', '.join(heater)}")
print(f"vent days ({len(vent)}): {', '.join(vent)}")
print(f"widest swing: day {widest + 1}, {lows[widest]} to {highs[widest]} C ({highs[widest] - lows[widest]} degrees)")
mid = float(sum(a + b for a, b in zip(lows, highs))) / (2.0 * float(len(lows)))
print(f"mean midpoint {mid:.1f} C")
print(f"coldest night {min(lows)} C")
