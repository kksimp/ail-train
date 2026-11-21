raw = [("choir", 9, 12, 120), ("yoga", 10, 11, 40), ("wedding", 11, 17, 300), ("chess", 12, 14, 90), ("dance", 13, 16, 150), ("quiz", 16, 19, 110), ("film", 17, 20, 130), ("band", 19, 23, 160)]
bs = sorted(raw, key=lambda b: b[2])

def last_before(bs, i):
    lo = 0
    hi = i - 1
    found = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if bs[mid][2] <= bs[i][1]:
            found = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return found

n = len(bs)
best = [0]
for i in range(n):
    p = last_before(bs, i)
    with_it = bs[i][3] + best[p + 1]
    best.append(max(best[i], with_it))
chosen = []
i = n - 1
while i >= 0:
    p = last_before(bs, i)
    if bs[i][3] + best[p + 1] >= best[i]:
        chosen.append(f"{bs[i][0]} {bs[i][1]}-{bs[i][2]}")
        i = p
    else:
        i -= 1
chosen.reverse()
for c in chosen:
    print(f"book {c}")
print(f"best takings: {best[n]}")
greedy = sorted(bs, key=lambda b: -b[3])
print(f"largest single fee: {greedy[0][0]} at {greedy[0][3]}")
