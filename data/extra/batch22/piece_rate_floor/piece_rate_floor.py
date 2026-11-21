def money(c):
    return f"{c // 100}.{c % 100:02d}"

days = [("Kim", 8, 230, 6), ("Kim", 8, 190, 4), ("Ola", 6, 120, 10), ("Ola", 8, 260, 2), ("Ben", 7, 140, 0)]
totals = {}
topups = {}
for name, hours, made, rejects in days:
    piece = (made - rejects) * 45
    topup = max(hours * 1200 - piece, 0)
    totals[name] = totals.get(name, 0) + piece + topup
    topups[name] = topups.get(name, 0) + topup
    print(f"{name} {hours}h, {made - rejects} good: pieces {money(piece):>6}, top-up {money(topup):>5}")
for name, t in totals.items():
    print(f"{name}: {money(t)} of which top-up {money(topups[name])}")
