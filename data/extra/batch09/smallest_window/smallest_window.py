def smallest(t, need):
    want = {}
    for c in need:
        want[c] = want.get(c, 0) + 1
    have = {}
    formed = 0
    required = len(want)
    best_start = -1
    best_len = len(t) + 1
    left = 0
    for right in range(len(t)):
        c = t[right]
        have[c] = have.get(c, 0) + 1
        if c in want and have[c] == want[c]:
            formed += 1
        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left
            d = t[left]
            have[d] -= 1
            if d in want and have[d] < want[d]:
                formed -= 1
            left += 1
    return "" if best_start < 0 else t[best_start:best_start + best_len]

cases = [("ADOBECODEBANC", "ABC"), ("this is a test string", "tist"), ("geeksforgeeks", "ork"), ("aaabbbccc", "abc"), ("hello", "xyz"), ("abbcabb", "abb")]
for text, need in cases:
    w = smallest(text, need)
    shown = "none" if w == "" else f"'{w}'"
    print(f"{need:<5} in '{text}': {shown}")
