tol = {'A': 1, 'B': 2, 'C': 5}
per = {'A': 12, 'B': 4, 'C': 1}
counts = [("A-100", 'A', 500, 496), ("A-220", 'A', 240, 236), ("B-310", 'B', 150, 147), ("B-415", 'B', 90, 87), ("C-502", 'C', 60, 63), ("C-777", 'C', 40, 45)]
good = 0
work = 0
for sku, cl, system, counted in counts:
    ok = abs(counted - system) * 100 <= system * tol[cl]
    if ok:
        good += 1
    work += per[cl]
    verdict = "within tolerance" if ok else "recount"
    print(f"{sku} ({cl}): system {system:>3}, counted {counted:>3}, off {counted - system:>2}: {verdict}")
print(f"{good} of {len(counts)} accurate; {work} counts a year, about {work * 10 // 12 // 10}.{work * 10 // 12 % 10} a month")
