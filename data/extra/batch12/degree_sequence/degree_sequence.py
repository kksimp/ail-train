def graphical(seq):
    ds = sorted(seq, reverse=True)
    while len(ds) > 0:
        d = ds[0]
        ds.pop(0)
        if d > len(ds):
            return False
        for i in range(d):
            ds[i] -= 1
            if ds[i] < 0:
                return False
        ds = sorted(ds, reverse=True)
    return True

parties = [[3, 3, 3, 3], [4, 3, 3, 2, 2], [3, 3, 3, 1], [5, 4, 3, 2, 1, 1], [2, 2, 2, 2, 2, 2], [4, 4, 4, 1, 1], [3, 2, 2, 1], [6, 1, 1, 1, 1, 1, 1]]
ok = 0
for p in parties:
    total = sum(p)
    if graphical(p):
        ok += 1
        print(f"{p}: possible, {total // 2} handshakes")
    elif total % 2 == 1:
        print(f"{p}: impossible, odd total {total}")
    else:
        print(f"{p}: impossible")
print(f"{ok} of {len(parties)} parties could happen")
