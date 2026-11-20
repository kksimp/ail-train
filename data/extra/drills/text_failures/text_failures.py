def parse_time(text):
    parts = text.split(":")
    if len(parts) != 2:
        raise ValueError(f"expected HH:MM, got '{text}'")
    try:
        h = int(parts[0])
    except ValueError:
        raise ValueError(f"bad hour '{parts[0]}'")
    try:
        m = int(parts[1])
    except ValueError:
        raise ValueError(f"bad minute '{parts[1]}'")
    if h < 0 or h > 23:
        raise ValueError(f"hour {h} out of range")
    if m < 0 or m > 59:
        raise ValueError(f"minute {m} out of range")
    return h * 60 + m

def span(a, b):
    x = parse_time(a)
    y = parse_time(b)
    if y < x:
        raise ValueError(f"{b} is before {a}")
    return y - x

for a, b in [("09:00", "17:30"), ("9:5", "9:50"), ("12:00", "11:00"), ("noon", "13:00"), ("10:00", "25:00"), ("08:xx", "09:00")]:
    try:
        m = span(a, b)
        print(f"{a}-{b}: {m // 60}h {m % 60}m")
    except ValueError as e:
        print(f"{a}-{b}: error: {e}")
print(0)
print(23 * 60 + 59)
