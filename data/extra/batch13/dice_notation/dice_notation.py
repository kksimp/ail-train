def parse(s):
    parts = s.split("d")
    if len(parts) != 2:
        return None, f"no single d in {s}"
    count_text = "1" if parts[0] == "" else parts[0]
    if not count_text.isdigit():
        return None, f"bad count in {s}"
    n = int(count_text)
    rest = parts[1]
    sides_text = rest
    bonus = 0
    if "+" in rest:
        i = rest.find("+")
        sides_text = rest[:i]
        bt = rest[i + 1:]
        if not bt.isdigit():
            return None, f"bad bonus in {s}"
        bonus = int(bt)
    elif "-" in rest:
        i = rest.find("-")
        sides_text = rest[:i]
        bt = rest[i + 1:]
        if not bt.isdigit():
            return None, f"bad bonus in {s}"
        bonus = -int(bt)
    if not sides_text.isdigit():
        return None, f"bad sides in {s}"
    sides = int(sides_text)
    if n < 1 or sides < 2:
        return None, f"too few dice or sides in {s}"
    return (n, sides, bonus), None

seed = 99
for text in ["3d6+2", "d20", "2d8-1", "4d4", "1d12+3", "2x6", "d1", "3d6+q"]:
    r, err = parse(text)
    if r is not None:
        count, sides, bonus = r
        mean = float(count * (sides + 1)) / 2.0 + float(bonus)
        total = bonus
        for k in range(count):
            seed = (seed * 1103515245 + 12345) % 2147483648
            total += (seed // 65536) % sides + 1
        print(f"{text:<7} min {count + bonus:>2} max {count * sides + bonus:>2} mean {mean:>4.1f} rolled {total}")
    else:
        print(f"{text:<7} error: {err}")
