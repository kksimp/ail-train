def balls(overs, all_out):
    if all_out:
        return 300
    parts = overs.split(".")
    whole = int(parts[0])
    extra = int(parts[1]) if len(parts) > 1 else 0
    return whole * 6 + extra

def nrr(s):
    return s[2] * 6.0 / s[3] - s[4] * 6.0 / s[5]

names = ["Lions", "Tigers", "Eagles", "Sharks"]
matches = [(0, 1, 268, "50", False, 240, "48.2", True), (2, 3, 301, "50", False, 255, "44.1", True), (0, 2, 230, "49.4", True, 231, "46.5", False), (1, 3, 199, "41.3", True, 200, "38", False), (0, 3, 275, "50", False, 276, "49.5", False), (1, 2, 288, "50", False, 250, "50", False)]
table = [[n, 0, 0, 0, 0, 0] for n in names]
for a, b, ra, oa, outa, rb, ob, outb in matches:
    ba = balls(oa, outa)
    bb = balls(ob, outb)
    table[a][2] += ra
    table[a][3] += ba
    table[a][4] += rb
    table[a][5] += bb
    table[b][2] += rb
    table[b][3] += bb
    table[b][4] += ra
    table[b][5] += ba
    if ra > rb:
        table[a][1] += 2
    else:
        table[b][1] += 2
ranked = sorted(table, key=lambda s: (-s[1], -int(nrr(s) * 1000000.0)))
for i, s in enumerate(ranked):
    print(f"{i + 1}. {s[0]:<7} {s[1]} pts  NRR {nrr(s):>6.3f}")
