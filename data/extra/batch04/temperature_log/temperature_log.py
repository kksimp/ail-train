good = []; bad = 0
for l in ["t=12", "t=15", "", "t=hot", "t=99", "t=-4", "temp 7", "t= 9"]:
    t = l.strip(); e = None
    if t == "": e = "empty line"
    else:
        p = t.split("=")
        if len(p) != 2: e = f"no value in {t}"
        else:
            try:
                v = int(p[1].strip())
                if v < -60 or v > 60: e = f"{v} is out of range"
            except ValueError: e = f"no value in {t}"
    if e: bad += 1; print(f"skipped: {e}")
    else: good.append(v)
print(f"{len(good)} good readings: {good}, low {min(good)}, high {max(good)}")
print(f"{bad} bad lines")
