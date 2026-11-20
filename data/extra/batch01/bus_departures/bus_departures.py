def clock(m):
    return f"{(m // 60) % 24:02d}:{m % 60:02d}"

def parse_clock(text):
    parts = text.split(":")
    if len(parts) != 2:
        return None
    try:
        h, m = int(parts[0]), int(parts[1])
    except ValueError:
        return None
    if h < 0 or h > 23 or m < 0 or m > 59:
        return None
    return h * 60 + m

times = []
t = 6 * 60 + 15
while t < 9 * 60:
    times.append(t)
    t += 25
print(f"buses: {len(times)}")
print(" ".join(clock(x) for x in times[:4]))
for asked in ["06:00", "07:41", "08:59", "9:5", "25:00"]:
    now = parse_clock(asked)
    if now is None:
        print(f"{asked}: not a time")
        continue
    nxt = next((x for x in times if x >= now), None)
    if nxt is not None:
        print(f"{asked}: next bus {clock(nxt)}, wait {nxt - now} min")
    else:
        print(f"{asked}: no more buses")
