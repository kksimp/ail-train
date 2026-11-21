T = [8.2, 6.9, 7.4, 10.1, 11.3, 9.0, 5.6, 3.2, 2.8, 4.1, 6.0, 7.7, 9.9, 12.4, 13.8, 14.9, 16.2, 15.1, 11.0, 9.3, 8.8]; W = []; s = 0.0
for i, t in enumerate(T):
    if t < 15.5: s += 15.5 - t
    if i % 7 == 6: W.append(s); s = 0.0
c = 0
for i, w in enumerate(W):
    print(f"week {i + 1}: {w:.1f} degree days, {w * 2.1:.0f} kWh")
    if w > W[c]: c = i
print(f"total {sum(W):.1f} degree days; coldest week {c + 1}")
