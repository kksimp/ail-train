def br(c):
    return (c[0] * 299 + c[1] * 587 + c[2] * 114) // 1000
def s(c):
    return f"rgb({c[0]}, {c[1]}, {c[2]})"
fixtures = [("red wash", (200, 0, 0)), ("blue wash", (0, 0, 180)), ("amber spot", (120, 80, 0)), ("white spot", (90, 90, 90))]
stage = (0, 0, 0)
for name, c in fixtures:
    stage = tuple(min(a + b, 255) for a, b in zip(stage, c))
    print(f"+ {name:<11} -> {s(stage)}, brightness {br(stage)}")
gel = (0, 60, 100)
f = tuple(max(a - b, 0) for a, b in zip(stage, gel))
print(f"through gel -> {s(f)}, brightness {br(f)}")
print(f"blackout -> {s((0, 0, 0))}")
