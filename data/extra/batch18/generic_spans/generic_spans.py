stays = [(3, 6), (7, 9), (5, 8), (12, 14)]
for i in range(4):
    for j in range(i + 1, 4):
        a, b = stays[i], stays[j]
        if a[0] <= b[1] and b[0] <= a[1]: print(f"bookings {i} and {j} clash")
print(f"night 8: {sum(1 for s in stays if s[0] <= 8 <= s[1])} rooms taken")
drawers = [("A", "Fz"), ("G", "Mz"), ("N", "Sz"), ("T", "Zz")]
for name in ["Okafor", "Brandt", "Gupta", "Zhou", "Moreau"]:
    found = -1
    for k, d in enumerate(drawers):
        if d[0] <= name <= d[1]: found = k
    print(f"{name} -> drawer {found + 1}")
