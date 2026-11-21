MOD = 1000000007

def repeat_at(s, cs, size):
    if size == 0:
        return 0
    top = 1
    for _ in range(size):
        top = top * 131 % MOD
    seen = {}
    h = 0
    for i in range(len(cs)):
        h = (h * 131 + ord(cs[i])) % MOD
        if i >= size:
            h = (h - ord(cs[i - size]) * top % MOD + MOD) % MOD
        if i >= size - 1:
            start = i - size + 1
            if h in seen:
                first = seen[h]
                if s[first:first + size] == s[start:start + size]:
                    return first
            else:
                seen[h] = start
    return -1

def longest(s):
    cs = list(s)
    lo = 0
    hi = len(cs) - 1
    best = 0
    pos = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        at = repeat_at(s, cs, mid)
        if at >= 0:
            best = mid
            pos = at
            lo = mid + 1
        else:
            hi = mid - 1
    return s[pos:pos + best]

for s in ["banana", "mississippi", "abcdefg", "to be or not to be", "abcabcabc", "the cat sat on the mat"]:
    r = longest(s)
    print(f"{s:<22} -> [{r}] ({len(r)} letters)")
