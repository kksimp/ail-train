def dive_score(marks, dd):
    mid = sorted(marks)[1:4]
    return sum(mid) * dd

def hundredths(n):
    return f"{n // 100}.{n % 100:02}"

divers = ["Ito", "Kerr", "Lund"]
dives = [[[75, 80, 70, 75, 85], [65, 70, 70, 60, 65], [80, 85, 85, 90, 80]], [[90, 85, 85, 90, 95], [55, 60, 50, 60, 55], [70, 75, 70, 70, 65]], [[70, 70, 75, 70, 70], [75, 80, 80, 75, 80], [60, 65, 65, 70, 60]]]
difficulty = [[28, 32, 30], [31, 34, 29], [27, 30, 33]]
totals = []
for d in range(3):
    total = 0
    parts = []
    for k in range(3):
        s = dive_score(dives[d][k], difficulty[d][k])
        total += s
        parts.append(hundredths(s))
    totals.append(total)
    shown = " + ".join(parts)
    print(f"{divers[d]:<5} {shown} = {hundredths(total)}")
order = sorted([0, 1, 2], key=lambda i: -totals[i])
for place, i in enumerate(order):
    print(f"{place + 1}. {divers[i]} {hundredths(totals[i])}")
