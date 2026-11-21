st = [("Depot", 12, 0), ("Market", 25, 3), ("School", 35, 8), ("Hospital", 6, 21), ("Park", 9, 4), ("Station", 14, 22), ("Harbour", 0, 43)]
l = 0; b = ("", 0)
for n, on, off in st:
    l += on - off
    print(f"{n:<9} +{on:<3} -{off:<3} on board {l:>2}" + ("  over capacity" if l > 60 else ""))
    if l > b[1]: b = (n, l)
print(f"busiest after {b[0]} with {b[1]}")
print(f"total trips: {sum(s[1] for s in st)}")
