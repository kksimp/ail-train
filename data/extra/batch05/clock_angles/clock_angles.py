def at(h, m):
    d = abs((h % 12) * 300 + m * 5 - m * 60)
    return 3600 - d if d > 1800 else d
for h, m in [(3, 0), (9, 45), (12, 30), (6, 0), (2, 20), (11, 59)]: a = at(h, m); print(f"{h}:{m:02} -> {a // 10}.{a % 10} degrees")
print("exactly opposite: " + " ".join(f"{h}:{m:02}" for h in range(12) for m in range(60) if at(h, m) == 1800))
