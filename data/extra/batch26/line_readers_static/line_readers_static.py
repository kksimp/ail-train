def coord(t):
    p = t.split(",")
    if len(p) != 2: return None
    try:
        return (int(p[0].strip()), int(p[1].strip()))
    except ValueError:
        return None
def span(t):
    p = t.split("-")
    if len(p) != 2: return None
    try:
        a, b = int(p[0].strip()), int(p[1].strip())
    except ValueError:
        return None
    if a > b: return None
    return (a, b)
def read_all(f, lines):
    out = []
    for l in lines:
        v = f(l)
        if v is not None:
            out.append(v)
        else:
            print(f"  skipped '{l}'")
    return out
print("coordinates:")
pts = read_all(coord, ["3,4", "x,1", "10, -2", "7"])
print("  read " + " ".join(f"({x}, {y})" for x, y in pts))
print("spans:")
spans = read_all(span, ["10-20", "5-3", "40-45", "a-b"])
print("  read " + " ".join(f"{a}..{b}" for a, b in spans) + f", total width {sum(b - a for a, b in spans)}")
