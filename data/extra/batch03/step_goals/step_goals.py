s = [8200, 10400, 12100, 9900, 11000, 10050, 14000, 6000, 10100, 10200, 10300, 10900, 7600, 13300, 10000, 9100, 4300, 15500, 10010, 10020, 8800, 11100, 12000, 9700, 10500, 10600, 10700, 10800]
g = 10000
print(f"goal met on {sum(1 for x in s if x >= g)} of {len(s)} days")
b = r = 0
for x in s:
    if x >= g: r += 1; b = max(b, r)
    else: r = 0
print(f"longest streak: {b} days")
w = [sum(s[i:i + 7]) for i in range(0, len(s), 7)]
print("weekly totals: " + " / ".join(f"{x:,}" for x in w))
print(f"best week: {w.index(max(w)) + 1} ({max(w):,})")
print(f"average: {sum(s) // len(s):,} a day")
