def binary(xs, target, lo, hi, probes):
    while lo < hi:
        mid = (lo + hi) // 2
        probes[0] += 1
        if xs[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def gallop(xs, target, probes):
    bound = 1
    while bound < len(xs):
        probes[0] += 1
        if xs[bound] >= target:
            break
        bound *= 2
    return binary(xs, target, bound // 2, min(bound, len(xs)), probes)

xs = [i * 3 + 1 for i in range(200)]
for t in [4, 10, 25, 301, 598, 1000]:
    g = [0]
    b = [0]
    at = gallop(xs, t, g)
    at2 = binary(xs, t, 0, len(xs), b)
    found = "found" if at < len(xs) and xs[at] == t else "absent"
    same = "true" if at == at2 else "false"
    print(f"target {t:>4}: index {at:>3} {found:<6} gallop {g[0]:>2} probes, binary {b[0]:>2} (same index {same})")
