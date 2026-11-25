import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


def compute(gross):
    pension = (gross * 5 + 50) // 100
    taxable = gross - pension
    low = min(taxable, 200000)
    high = taxable - low
    tax = (low * 10 + 50) // 100 + (high * 20 + 50) // 100
    social = (min(gross, 600000) * 62 + 500) // 1000
    return [gross, pension, tax, social, gross - pension - tax - social]


def row(label, p):
    return label + "\t" + "\t".join(money(x) for x in p)


def main():
    rows = []
    total = [0] * 5
    for k, line in enumerate(sys.stdin.read().splitlines(), 1):
        w = line.split()
        if not w:
            continue
        g = toi(w[1]) if len(w) > 1 else None
        if len(w) != 2 or g is None or g < 0 or g > 10000000:
            print("line %d: bad record" % k)
            continue
        p = compute(g)
        rows.append((w[0], p))
        total = [a + b for a, b in zip(total, p)]
    print("name\tgross\tpension\ttax\tsocial\tnet")
    for name, p in rows:
        print(row(name, p))
    print(row("TOTAL", total))


main()
