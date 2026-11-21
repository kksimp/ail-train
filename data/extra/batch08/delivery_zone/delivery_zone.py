def inside(px, py, x, y):
    hit = False; j = len(px) - 1
    for i in range(len(px)):
        if (py[i] > y) != (py[j] > y):
            if x < (px[j] - px[i]) * (y - py[i]) / (py[j] - py[i]) + px[i]: hit = not hit
        j = i
    return hit
px = [0.0, 10.0, 10.0, 6.0, 6.0, 0.0]; py = [0.0, 0.0, 4.0, 4.0, 9.0, 9.0]
adds = [("12 Mill Rd", 2.0, 2.0), ("3 Oak Ave", 8.0, 6.0), ("40 Quay St", 5.0, 7.5), ("7 Bell Ln", 9.5, 3.5), ("19 High St", -1.0, 4.0), ("2 Ford Way", 6.5, 4.5)]
c = 0
for n, x, y in adds:
    ok = inside(px, py, x, y); c += ok
    print(f"{n:<11} ({x}, {y}): {'deliver' if ok else 'out of zone'}")
print(f"{c} of {len(adds)} in the zone")
