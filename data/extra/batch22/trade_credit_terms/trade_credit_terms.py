def parse(t):
    parts = t.split(" ")
    if len(parts) != 3 or parts[1] != "net":
        return None, f"expected D/N net M, got '{t}'"
    left = parts[0].split("/")
    if len(left) != 2:
        return None, f"bad discount part '{parts[0]}'"
    if not left[0].isdigit():
        return None, f"bad percent '{left[0]}'"
    if not left[1].isdigit():
        return None, f"bad days '{left[1]}'"
    if not parts[2].isdigit():
        return None, f"bad net days '{parts[2]}'"
    d, e, n = int(left[0]), int(left[1]), int(parts[2])
    if n <= e:
        return None, "net days must be more than discount days"
    return (d, e, n), None

for s in ["2/10 net 30", "1/10 net 30", "3/15 net 60", "2/10 net 45", "2/10 net 10", "net 30", "x/10 net 30"]:
    t, err = parse(s)
    if t:
        d, e, n = t
        per = float(d) / float(100 - d)
        periods = 365.0 / float(n - e)
        simple = per * periods * 100.0
        compound = ((1.0 + per) ** periods - 1.0) * 100.0
        print(f"{s:<12} simple {simple:>5.1f}% a year, compounded {compound:>5.1f}%")
    else:
        print(f"{s:<12} rejected: {err}")
