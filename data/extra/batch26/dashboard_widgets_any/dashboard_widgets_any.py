def level(v):
    return "_" if v <= 2 else "." if v <= 5 else "-" if v <= 7 else "^"
def render(t, body, alert):
    return f"[{t:<9}] {body}{' !' if alert else ''}"
def gauge(p):
    f = p // 10
    return "#" * f + "." * (10 - f) + f" {p}%"
print(render("disk", gauge(73), True))
print(render("signups", "".join(level(v) for v in [3, 5, 2, 8, 9, 4, 1, 6]), False))
print(render("cpu", gauge(18), False))
print("3 widgets, 1 alert")
