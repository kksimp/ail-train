def per_cm(cm, per10):
    return (cm * per10 + 5) // 10

def to_multiple(n, m):
    return (n + m // 2) // m * m

def tenths(t):
    return f"{t // 10}.{t % 10}"

for name, chest, length in [("S", 86, 60), ("M", 96, 63), ("L", 106, 66), ("XL", 116, 69)]:
    width = (chest + 8) // 2
    cast = to_multiple(per_cm(width, 22), 4)
    body = per_cm(length, 30)
    print(f"{name:<2} chest {chest}: cast on {cast}, {body} rows; panel {tenths(cast * 100 // 22)} cm (at 24 st: {tenths(cast * 100 // 24)} cm)")
print("rib needs a multiple of 4: every cast-on above divides evenly")
