def longest_run(s, c):
    best = 0
    cur = 0
    for x in s:
        if x == c:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best

def outages(s):
    n = 0
    prev = 'U'
    for x in s:
        if x == 'D' and prev != 'D':
            n += 1
        prev = x
    return n

probes = [("api", "UUUUUUUUUUDDUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"), ("db", "UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"), ("cache", "UUUDUUUUDDDUUUUUUUUUUUUUDUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"), ("mail", "DDDDDDUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUDDDD")]
for name, s in probes:
    total = len(s)
    up = s.count("U")
    pct = float(up * 100) / float(total)
    verdict = "ok" if up * 100 >= total * 99 else "BELOW 99%"
    print(f"{name:<6} {pct:>6.2f}% up, {outages(s)} outages, longest {longest_run(s, 'D')} min  {verdict}")
