def parse(s):
    parts = s.split("-")
    if len(parts) != 2:
        return None, f"no dash in {s}"
    if not parts[0].isdigit():
        return None, f"bad goals in {s}"
    if not parts[1].isdigit():
        return None, f"bad points in {s}"
    return 3 * int(parts[0]) + int(parts[1]), None

games = [("Corrib", "1-14", "Shannon", "2-09"), ("Liffey", "0-18", "Corrib", "3-09"), ("Shannon", "2-12", "Liffey", "1-15"), ("Corrib", "2-x", "Liffey", "0-10"), ("Shannon", "0-20", "Corrib", "4-07"), ("Liffey", "1-13", "Shannon", "0-13")]
pts = {}
diff = {}
for home, hs, away, aws in games:
    h, err = parse(hs)
    if err:
        print(f"skipped {home} v {away}: {err}")
        continue
    a, err = parse(aws)
    if err:
        print(f"skipped {home} v {away}: {err}")
        continue
    diff[home] = diff.get(home, 0) + h - a
    diff[away] = diff.get(away, 0) + a - h
    if h > a:
        pts[home] = pts.get(home, 0) + 2
        pts[away] = pts.get(away, 0)
    elif a > h:
        pts[away] = pts.get(away, 0) + 2
        pts[home] = pts.get(home, 0)
    else:
        pts[home] = pts.get(home, 0) + 1
        pts[away] = pts.get(away, 0) + 1
    print(f"{home} {hs} ({h}) v {away} {aws} ({a})")
for t in sorted(pts.keys(), key=lambda t: (-pts[t], -diff[t])):
    print(f"{t:<8} {pts[t]} pts, difference {diff[t]}")
