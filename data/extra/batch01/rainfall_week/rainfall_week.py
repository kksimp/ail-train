import math
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
rain = [2.5, 0.0, 11.25, 4.0, 0.5, 7.75, 3.0]
print(f"total {sum(rain):.1f} mm, mean {sum(rain) / len(rain):.2f} mm")
w = 0
for i in range(1, len(rain)):
    if rain[i] > rain[w]:
        w = i
print(f"wettest day: {DAYS[w]} ({rain[w]:.1f} mm)")
print("dry days: " + ", ".join(DAYS[i] for i in range(len(rain)) if rain[i] < 1.0))
best = (0, -1.0)
for i in range(len(rain) - 2):
    t = sum(rain[i:i + 3])
    if t > best[1]:
        best = (i, t)
print(f"wettest run: {DAYS[best[0]]}-{DAYS[best[0] + 2]} {best[1]:.1f} mm")
def round_away(x):
    return math.floor(x + 0.5) if x >= 0 else -math.floor(-x + 0.5)
for i, r in enumerate(rain):
    print(f"{DAYS[i]} {r:>6.2f} " + "#" * int(round_away(r / 2.0)))
