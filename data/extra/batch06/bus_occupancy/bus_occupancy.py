l = 0; pk = ("", 0); ov = []
for n, a, b in [("Depot", 18, 0), ("Market", 22, 3), ("School", 31, 9), ("Hospital", 6, 14), ("Station", 25, 20), ("Park", 4, 30), ("Docks", 0, 30)]:
    l = l - b + a; print(f"{n:<9} +{a:<2} -{b:<2} load {l}")
    if l > pk[1]: pk = (n, l)
    if l > 60: ov.append(n)
print(f"busiest after {pk[0]} ({pk[1]}); over seats at: {', '.join(ov) if ov else 'none'}")
