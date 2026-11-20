def lp(s):
    best = (0, 0)
    for i in range(len(s)):
        for lo, hi in [(i, i), (i, i + 1)]:
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1; hi += 1
            if hi - (lo + 1) > best[1] - best[0]: best = (lo + 1, hi)
    return s[best[0]:best[1]]
for s in ["babad", "cbbd", "forgeeksskeegfor", "a", "", "abacdfgdcaba", "racecar level"]:
    p = lp(s)
    print(f"'{s}': '{p}' ({len(p)})")
