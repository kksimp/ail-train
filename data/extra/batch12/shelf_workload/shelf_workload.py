def readers_needed(pages, limit):
    count = 1
    load = 0
    for p in pages:
        if load + p > limit:
            count += 1
            load = p
        else:
            load += p
    return count

def smallest_limit(pages, k):
    lo = max(pages)
    hi = sum(pages)
    while lo < hi:
        mid = (lo + hi) // 2
        if readers_needed(pages, mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo

pages = [120, 340, 90, 410, 260, 180, 75, 300, 220, 150]
print(f"shelves: {pages}")
for k in [2, 3, 4, 5]:
    limit = smallest_limit(pages, k)
    groups = []
    load = 0
    first = 1
    for i, p in enumerate(pages):
        if load + p > limit:
            groups.append(f"{first}-{i}:{load}")
            first = i + 1
            load = p
        else:
            load += p
    groups.append(f"{first}-{len(pages)}:{load}")
    print(f"{k} readers, at most {limit} pages: {' '.join(groups)}")
