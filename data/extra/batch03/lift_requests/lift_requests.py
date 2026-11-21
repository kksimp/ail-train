def serve(s, up, req):
    p = sorted(req); at = s; v = []
    while p:
        ah = [f for f in p if f >= at] if up else [f for f in p if f <= at][::-1]
        if not ah: up = not up; continue
        t = ah[0]; v.append(t); at = t; p.remove(t)
    return v
def tr(s, v):
    tot = 0; at = s
    for x in v: tot += abs(x - at); at = x
    return tot
for s, up in [(5, True), (5, False), (0, True)]:
    v = serve(s, up, [7, 2, 9, 4, 12, 1])
    print(f"from {s} {'up' if up else 'down'}: {v}, {tr(s, v)} floors")
