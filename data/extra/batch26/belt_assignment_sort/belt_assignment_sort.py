arr = [("EZ214", 5, 150, False), ("BA331", 0, 210, True), ("FR882", 12, 180, False), ("LH907", 5, 240, True), ("KL112", 20, 90, True), ("U2310", 25, 120, False)]
arr.sort(key=lambda a: (a[1], a[0]))
def clock(m):
    t = 14 * 60 + m
    return f"{t // 60:02}:{t % 60:02}"
free = [0, 0, 0]
for f, l, bags, intl in arr:
    allowed = 2 if intl else 3
    b = 0
    for k in range(1, allowed):
        if free[k] < free[b]: b = k
    start = max(l + 10, free[b])
    free[b] = start + bags // 30 + 5
    print(f"{f} landed {clock(l)}: belt {b + 1}, {clock(start)}-{clock(free[b])}")
print(f"most bags: {', '.join(a[0] for a in sorted(arr, key=lambda a: (-a[2], a[0]))[:2])}")
