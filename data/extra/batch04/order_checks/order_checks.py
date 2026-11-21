def pl(l):
    p = l.split("x")
    if len(p) != 2: return None, "expected QTYxPRICE"
    try: q = int(p[0].strip())
    except ValueError: return None, "bad quantity"
    try: pr = int(p[1].strip())
    except ValueError: return None, "bad price"
    if q <= 0: return None, "quantity must be positive"
    return q * pr, None
for o in [["2x150", "1x999", "3x20"], ["1x100", "two x 5"], ["4x25", "0x10"], ["5"]]:
    t = 0; e = None
    for i, l in enumerate(o):
        v, er = pl(l)
        if er: e = f"line {i + 1}: {er}"; break
        t += v
    s = "[" + ", ".join(f'"{x}"' for x in o) + "]"
    print(f"{s}: rejected, {e}" if e else f"{s}: total {t}")
