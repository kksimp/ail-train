samples = [[2501, 2503, 2499, 2500], [2498, 2502, 2500, 2501], [2504, 2500, 2502, 2503], [2497, 2499, 2501, 2498], [2502, 2505, 2503, 2504], [2500, 2498, 2501, 2499], [2509, 2507, 2510, 2508], [2499, 2501, 2500, 2502]]
means = []
ranges = []
for s in samples:
    means.append(float(sum(s)) / 4.0)
    ranges.append(max(s) - min(s))
grand = 0.0
for m in means:
    grand = grand + m
grand = grand / 8.0
rbar = float(sum(ranges)) / 8.0
upper = grand + 0.729 * rbar
lower = grand - 0.729 * rbar
r_upper = 2.282 * rbar
print(f"grand mean {grand:.3f}, mean range {rbar:.3f}")
print(f"mean limits {lower:.2f} to {upper:.2f}, range limit {r_upper:.2f}")
for i in range(8):
    m = means[i]
    if m > upper or m < lower:
        flag = " <- mean out"
    elif float(ranges[i]) > r_upper:
        flag = " <- range out"
    else:
        flag = ""
    print(f"sample {i + 1}: mean {m:.2f}, range {ranges[i]}{flag}")
