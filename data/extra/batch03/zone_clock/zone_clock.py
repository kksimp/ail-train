def loc(u, o):
    t = u + o; d = "-1 day" if t < 0 else "+1 day" if t >= 1440 else ""
    m = t % 1440; s = f"{m // 60:02d}:{m % 60:02d}"
    return s if not d else f"{s} ({d})"
C = [("London", 0), ("Oslo", 60), ("Kolkata", 330), ("Tokyo", 540), ("Auckland", 780), ("New York", -300), ("Honolulu", -600)]
for h, mi in [(9, 30), (22, 0)]:
    u = h * 60 + mi; print(f"meeting at {h:02d}:{mi:02d} UTC")
    for n, o in C: print(f"  {n:<9} {loc(u, o)}")
