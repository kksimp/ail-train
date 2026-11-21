def project(n, births, survive):
    nxt = []
    newborns = 0.0
    for i in range(len(n)):
        newborns += births[i] * n[i]
    nxt.append(newborns)
    for i in range(len(survive)):
        nxt.append(survive[i] * n[i])
    return nxt

def total(n):
    acc = 0.0
    for x in n:
        acc = acc + x
    return acc

births = [0.0, 1.5, 2.0, 0.8]
survive = [0.5, 0.7, 0.4]
n = [100.0, 0.0, 0.0, 0.0]
ratio = 0.0
for year in range(16):
    if year % 3 == 0:
        cells = " ".join(f"{x:>7.1f}" for x in n)
        print(f"year {year:>2}: {cells}  total {total(n):>8.1f}")
    nxt = project(n, births, survive)
    ratio = total(nxt) / total(n)
    n = nxt
print(f"growth ratio settles near {ratio:.4f} a year")
t = total(n)
shares = ", ".join(f"{x / t * 100.0:.1f}%" for x in n)
print(f"stable age mix: {shares}")
