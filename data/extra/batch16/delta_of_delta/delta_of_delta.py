def cost(dod):
    if dod == 0:
        return 1
    if -63 <= dod <= 64:
        return 9
    if -255 <= dod <= 256:
        return 12
    if -2047 <= dod <= 2048:
        return 16
    return 36

ts = [1000, 1060, 1120, 1180, 1241, 1300, 1360, 1420, 1500, 1560, 1620, 1620, 1680, 4000]
bits = 64 + 14
prev_delta = ts[1] - ts[0]
parts = []
for i in range(2, len(ts)):
    delta = ts[i] - ts[i - 1]
    dod = delta - prev_delta
    c = cost(dod)
    bits += c
    parts.append(f"{dod}:{c}")
    prev_delta = delta
print(f"first time stored whole (64 bits), first gap {ts[1] - ts[0]} (14 bits)")
for k in range(0, len(parts), 6):
    print("  " + "  ".join(parts[k:k + 6]))
raw = 64 * len(ts)
print(f"{len(ts)} timestamps: {bits} bits instead of {raw}")
