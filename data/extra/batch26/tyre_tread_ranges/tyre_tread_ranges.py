def verdict(v):
    if v <= 15: return "illegal"
    if v <= 29: return "replace soon"
    if v <= 59: return "fine"
    if v <= 80: return "nearly new"
    return "recheck"
mm = lambda v: f"{v // 10}.{v % 10}"
cars = [("KX19 ABC", [72, 70, 31, 29]), ("LM65 XYZ", [15, 40, 41, 39]), ("PR70 DEF", [88, 65, 66, 64])]
p = 0
for plate, ts in cars:
    print(f"{plate}: {' | '.join(f'{mm(t)} {verdict(t)}' for t in ts)}")
    if not any(verdict(t) == "illegal" for t in ts): p += 1
print(f"{p} of {len(cars)} cars pass, shallowest tread {mm(min(t for _, ts in cars for t in ts))} mm")
