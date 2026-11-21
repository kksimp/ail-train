def radii(cs, even):
    n = len(cs)
    d = [0] * n
    shift = 1 if even else 0
    l = 0
    r = -1
    for i in range(n):
        k = 0 if even else 1
        if i <= r:
            k = min(d[l + r - i + shift], r - i + 1)
        while i - k - shift >= 0 and i + k < n and cs[i - k - shift] == cs[i + k]:
            k += 1
        d[i] = k
        if i + k - 1 > r:
            l = i - k + 1 - shift
            r = i + k - 1
    return d

for w in ["abacaba", "aabbaa", "forgeeksskeegfor", "racecars", "noon"]:
    odd = radii(w, False)
    even = radii(w, True)
    count = sum(odd) + sum(even)
    best_len = 0
    best_at = 0
    for i in range(len(w)):
        if 2 * odd[i] - 1 > best_len:
            best_len = 2 * odd[i] - 1
            best_at = i - odd[i] + 1
        if 2 * even[i] > best_len:
            best_len = 2 * even[i]
            best_at = i - even[i]
    longest = w[best_at:best_at + best_len]
    print(f"{w:<17} {count:>3} palindromic pieces, longest '{longest}'")
print("odd radii of abacaba: " + " ".join(str(v) for v in radii("abacaba", False)))
