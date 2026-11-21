orders = [(75, "Okoro"), (30, "Batista"), (30, "Chen"), (120, "Dahl"), (50, "Evans"), (95, "Ford")]
def clock(m):
    t = 9 * 60 + m
    return f"{t // 60:02}:{t % 60:02}"
s = sorted(orders)
print(f"ready order: {', '.join(n for _, n in s)}")
i = 0
for tick in [30, 60, 90, 120]:
    h = []
    while i < len(s) and s[i][0] <= tick:
        h.append(f"{s[i][1]} (ready {clock(s[i][0])})"); i += 1
    print(f"{clock(tick)}: {', '.join(h) if h else 'nobody'}")
print(f"left on the shelf: {len(s) - i}")
