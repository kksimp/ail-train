for n in [9, 529, 20, 15, 32, 1041, 0, 561892]:
    b = f"{n:b}"
    g = max((len(x) for x in b.strip("0").split("1")), default=0)
    print(f"{n:>7} {b:>20} gap {g}")
