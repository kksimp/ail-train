def longest(r, ok):
    b = run = 0
    for c in r:
        if ok(c):
            run += 1; b = max(b, run)
        else:
            run = 0
    return b
def cur(r):
    if not r: return "none"
    n = 0
    for c in reversed(r):
        if c != r[-1]: break
        n += 1
    return f"{n}{r[-1]}"
for s in ["WWDLWWWLDDW", "LLLL", "WDWDWDW", "", "DWWWWWL"]:
    print(f"'{s}': best win run {longest(s, lambda c: c == 'W')}, unbeaten {longest(s, lambda c: c != 'L')}, now {cur(s)}")
