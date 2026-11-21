def subset_sums(ws):
    sums = [0]
    for w in ws:
        sums = sums + [s + w for s in sums]
    return sums

def best_below(sorted_sums, cap):
    lo = 0
    hi = len(sorted_sums) - 1
    found = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_sums[mid] <= cap:
            found = sorted_sums[mid]
            lo = mid + 1
        else:
            hi = mid - 1
    return found

weights = [173, 241, 88, 412, 305, 157, 69, 230, 391, 126, 284, 47, 358, 199, 263, 115]
limit = 2000
left = subset_sums(weights[0:8])
right = sorted(subset_sums(weights[8:]))
print(f"{len(left)} sums per half instead of {len(left) * len(right)} subsets")
best = 0
best_left = 0
for s in left:
    if s <= limit:
        r = best_below(right, limit - s)
        if s + r > best:
            best = s + r
            best_left = s
print(f"best load {best} of {limit}, left half gives {best_left}")
for cap in [500, 1000, 3000]:
    print(f"limit {cap}: right half alone reaches {best_below(right, cap)}")
