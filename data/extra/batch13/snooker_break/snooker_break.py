def value(ball):
    return {'R': 1, 'Y': 2, 'G': 3, 'N': 4, 'B': 5, 'P': 6, 'K': 7}.get(ball, 0)

def run_break(balls, st):
    total = 0
    want_colour = False
    for ball in balls:
        v = value(ball)
        if v == 0:
            return None, f"unknown ball {ball}"
        if st["reds"] > 0 or want_colour:
            if v == 1 and want_colour:
                return None, "red after red"
            if v > 1 and not want_colour:
                return None, "colour without a red"
            if v == 1:
                st["reds"] -= 1
            want_colour = v == 1
        else:
            if v != st["next"]:
                return None, "colour out of order"
            st["next"] += 1
        total += v
    return total, None

def left_on_table(reds, next_colour):
    colours = sum(range(next_colour, 8))
    return reds * 8 + colours

st = {"reds": 15, "next": 2}
breaks = ["RKRKRPRKRB", "RKRKRY", "RG", "RKRKRBRKRKRP", "KR", "YGN", "BPK"]
for i, b in enumerate(breaks):
    pts, err = run_break(b, st)
    if err is None:
        print(f"break {i + 1}: {pts:>3} points, {st['reds']:>2} reds left, {left_on_table(st['reds'], st['next']):>3} left to score")
    else:
        print(f"break {i + 1}: foul, {err}")
