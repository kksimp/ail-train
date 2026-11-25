import sys

LIMIT = 5000

def is_digits(s):
    return len(s) > 0 and all(c in "0123456789" for c in s)

coins = set()
have = False
queries = []
for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    if not have:
        have = True
        for w in t.split():
            if is_digits(w) and int(w) > 0:
                coins.add(int(w))
        continue
    queries.append(t)
dp = [0] * (LIMIT + 1)
dp[0] = 1
for c in sorted(coins):
    for a in range(c, LIMIT + 1):
        dp[a] += dp[a - c]
for q in queries:
    if is_digits(q) and len(q) <= 9:
        a = int(q)
        print(f"{a} too large" if a > LIMIT else f"{a} {dp[a]}")
    else:
        print(f"{q} invalid")
