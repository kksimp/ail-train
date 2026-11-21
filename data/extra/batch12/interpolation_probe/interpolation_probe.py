def binary_probes(xs, want):
    lo = 0
    hi = len(xs) - 1
    probes = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        probes += 1
        if xs[mid] == want:
            return [mid, probes]
        if xs[mid] < want:
            lo = mid + 1
        else:
            hi = mid - 1
    return [-1, probes]

def interp_probes(xs, want):
    lo = 0
    hi = len(xs) - 1
    probes = 0
    while lo <= hi and want >= xs[lo] and want <= xs[hi]:
        pos = lo
        if xs[hi] != xs[lo]:
            pos = lo + (want - xs[lo]) * (hi - lo) // (xs[hi] - xs[lo])
        probes += 1
        if xs[pos] == want:
            return [pos, probes]
        if xs[pos] < want:
            lo = pos + 1
        else:
            hi = pos - 1
    return [-1, probes]

seed = 7
even = []
for i in range(500):
    seed = (seed * 1103515245 + 12345) % 2147483648
    even.append(10000 + i * 40 + seed % 30)
squares = [i * i for i in range(1, 501)]
for want in [even[17], even[250], even[431], 25013]:
    b = binary_probes(even, want)
    t = interp_probes(even, want)
    print(f"even ids, find {want}: at {b[0]}, halving {b[1]} probes, guessing {t[1]} probes")
for want in [squares[3], squares[399]]:
    b = binary_probes(squares, want)
    t = interp_probes(squares, want)
    print(f"square ids, find {want}: halving {b[1]} probes, guessing {t[1]} probes")
