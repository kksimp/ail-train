B = [("823.9", "Hard Times", 4), ("510.2", "Number Sense", 3), ("940.5", "The Blitz", 6), ("823.1", "Emma", 5), ("599.9", "Primates", 7), ("510.9", "Geometry Now", 2), ("641.5", "Bread", 3), ("823.9", "Bleak House", 8)]
s = 1; u = 0; n = []
for c, t, w in sorted(B):
    if u + w > 14: print(f"shelf {s} ({u} cm): {' | '.join(n)}"); s += 1; u = 0; n = []
    u += w; n.append(f"{c} {t}")
print(f"shelf {s} ({u} cm): {' | '.join(n)}")
