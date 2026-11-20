band = [("drum (14 in)", 1, None), ("flute", 19, None), ("piano", 84, "a grand piano over 7 octaves"), ("drum (22 in)", 1, None)]
for n, k, d in band:
    print(d if d else f"{n} plays {k} notes")
print(f"total notes: {sum(k for _, k, _ in band)}")
best, most = "", -1
for n, k, _ in band:
    if k > most: most, best = k, n
print(f"widest range: {best}")
