def values():
    m = {}
    for i, c in enumerate("ABCDEFGH"):
        m[c] = i + 1
    for i, c in enumerate("JKLMN"):
        m[c] = i + 1
    m['P'] = 7
    m['R'] = 9
    for i, c in enumerate("STUVWXYZ"):
        m[c] = i + 2
    return m

def expected(vin):
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    table = values()
    if len(vin) != 17:
        return None, f"length {len(vin)}, not 17"
    total = 0
    for i, c in enumerate(vin):
        v = int(c) if c.isdigit() else table.get(c, -1)
        if v < 0:
            return None, f"letter {c} is not allowed"
        total += v * weights[i]
    r = total % 11
    return ("X" if r == 10 else str(r)), None

for vin in ["1M8GDM9AXKP042788", "11111111111111111", "1M8GDM9A1KP042788", "5GZCZ43D13S812715", "1HGCM82633A00435", "JH4KA7650MC0O1234"]:
    c, err = expected(vin)
    if c is not None:
        given = vin[8:9]
        verdict = "valid" if given == c else "wrong check digit"
        print(f"{vin:<18} needs {c}, has {given}: {verdict}")
    else:
        print(f"{vin:<18} rejected: {err}")
