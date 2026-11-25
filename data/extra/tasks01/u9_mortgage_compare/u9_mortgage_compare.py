import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


def simulate(principal, rate, years, pay):
    n = years * 12
    bal = principal
    months = interest = paid = 0
    while bal > 0 and months < n:
        i = (bal * rate + 60000) // 120000
        due = bal + i
        p = min(due, pay)
        interest += i
        paid += p
        bal = due - p
        months += 1
    return (0 if bal > 0 else months), interest, paid


def main():
    plans = []
    for k, line in enumerate(sys.stdin.read().splitlines(), 1):
        if not line.strip():
            continue
        w = line.split()
        v = [toi(x) for x in w[1:]] if len(w) == 4 else None
        if v is None or None in v or not (1 <= v[0] <= 500000000 and 0 <= v[1] <= 3000 and 1 <= v[2] <= 40):
            print("line %d: bad offer" % k)
            continue
        p, r, y = v
        lo, hi = 1, p * 2 + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if simulate(p, r, y, mid)[0] > 0:
                hi = mid
            else:
                lo = mid + 1
        months, interest, paid = simulate(p, r, y, lo)
        plans.append((w[0], lo, months, interest, paid))
    ranked = sorted(plans, key=lambda t: t[3])
    for i, (name, pay, months, interest, paid) in enumerate(ranked, 1):
        print("%d. %s payment %s months %d interest %s total %s" % (i, name, money(pay), months, money(interest), money(paid)))
    spread = ranked[-1][3] - ranked[0][3] if ranked else 0
    print("spread: " + money(spread))


main()
