X = [3, 8, 15, 21, 34, 42, 57, 63, 71, 88, 94]
for t in [42, 3, 94, 50, 1, 100]:
    lo, hi, pr, f = 0, len(X), [], False
    while lo < hi:
        m = (lo + hi) // 2; pr.append(X[m])
        if X[m] == t: f = True; lo = m; break
        if X[m] < t: lo = m + 1
        else: hi = m
    p = " ".join(map(str, pr))
    print(f"{t}: found at {lo} (probes {p})" if f else f"{t}: missing, insert at {lo} (probes {p})")
