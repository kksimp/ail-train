def to_decimal(text):
    p = text.split(" ")
    if len(p) != 4:
        return None, f"need 4 parts in '{text}'"
    d, m, s = int(p[0]), int(p[1]), int(p[2])
    if m >= 60 or s >= 60:
        return None, "minutes and seconds must be below 60"
    limit = 90 if p[3] in ("N", "S") else 180
    if d > limit:
        return None, f"{d} degrees is beyond {limit}"
    value = float(d) + float(m) / 60.0 + float(s) / 3600.0
    return (-value if p[3] in ("S", "W") else value), None

def to_dms(value, pos, neg):
    total = int(round(abs(value) * 3600.0))
    hemi = neg if value < 0.0 else pos
    return f"{total // 3600} {total % 3600 // 60} {total % 60} {hemi}"

for text in ["40 26 46 N", "79 58 56 W", "33 51 54 S", "151 12 34 E", "51 30 0 N", "12 75 0 E", "95 0 0 N", "1 2 E"]:
    v, err = to_decimal(text)
    if v is not None:
        print(f"{text:<12} -> {v:>11.5f}")
    else:
        print(f"{text:<12} -> error: {err}")
for v in [48.8584, -22.9519, 0.5]:
    print(f"{v:>8.4f} -> {to_dms(v, 'N', 'S')}")
