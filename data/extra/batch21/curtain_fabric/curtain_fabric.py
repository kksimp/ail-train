windows = [("lounge", 240, 230, 20, 64), ("bedroom", 160, 140, 25, 0), ("kitchen", 110, 90, 20, 32), ("nursery", 180, 200, 25, 45)]

def cut_drop(drop, rep):
    raw = drop + 25
    if rep == 0:
        return raw
    return (raw + rep - 1) // rep * rep

def metres(cm):
    return f"{cm // 100}.{cm % 100:02d} m"

total_cm = 0
for room, track, drop, full, rep in windows:
    n = (track * full + 1370 - 1) // 1370
    cut = cut_drop(drop, rep)
    cm = n * cut
    total_cm += cm
    print(f"{room:<8} fullness {full // 10}.{full % 10}: {n} widths x {cut} cm = {metres(cm)}")
cost = total_cm * 1895 // 100
print(f"buy {metres(total_cm)} at 18.95 a metre: {cost // 100}.{cost % 100:02d}")
