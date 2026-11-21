names = ["North", "Coast", "Capital", "Valley", "South"]
flows = [[0, 1200, 5400, 800, 300], [900, 0, 3100, 600, 700], [2100, 2600, 0, 1900, 2400], [500, 400, 2900, 0, 650], [350, 900, 1800, 700, 0]]
n = len(names)
biggest = (0, 0)
for i in range(n):
    outflow = sum(flows[i])
    inflow = sum(row[i] for row in flows)
    net = inflow - outflow
    gross = inflow + outflow
    eff = net / gross * 100.0
    print(f"{names[i]:<8} in {inflow:>6,} out {outflow:>6,} net {net:>6} gross {gross:>6,} efficiency {eff:>6.1f}%")
    for j in range(n):
        if flows[i][j] > flows[biggest[0]][biggest[1]]:
            biggest = (i, j)
total = sum(sum(row) for row in flows)
print(f"{total:,} movers; largest stream {names[biggest[0]]} -> {names[biggest[1]]} ({flows[biggest[0]][biggest[1]]:,})")
