def seconds(text):
    if len(text) < 2 or text[0] != 'P':
        return None, "needs P and at least one part"
    total = 0
    num = []
    in_time = False
    parts = 0
    for c in text[1:]:
        if c.isdigit():
            num.append(c)
            continue
        if c == 'T':
            in_time = True
            continue
        if not num:
            return None, f"unit {c} has no number"
        n = int("".join(num))
        num = []
        table = {'Y': (-1, 31536000), 'W': (-1, 604800), 'D': (-1, 86400), 'H': (3600, -1), 'M': (60, 2592000), 'S': (1, -1)}
        if c in table:
            size = table[c][0] if in_time else table[c][1]
        else:
            size = -1
        if size < 0:
            return None, f"unit {c} not allowed here"
        total += n * size
        parts += 1
    if num or parts == 0:
        return None, "number without a unit"
    return total, None

for d in ["PT45S", "PT1H30M", "P1DT2H30M", "P3W", "P1M", "PT1M", "P1Y2M10DT2H30M", "P", "PT5X", "P2H"]:
    s, err = seconds(d)
    if s is not None:
        print(f"{d:<15} {s:>9} seconds ({s // 3600} h {s % 3600 // 60} min)")
    else:
        print(f"{d:<15} error: {err}")
