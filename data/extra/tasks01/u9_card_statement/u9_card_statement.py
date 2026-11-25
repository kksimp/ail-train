import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    sign = "-" if c < 0 else ""
    a = abs(c)
    return "%s%d.%02d" % (sign, a // 100, a % 100)


def min_payment(bal):
    if bal <= 0:
        return 0
    if bal <= 2500:
        return bal
    return max(2500, (bal * 2 + 99) // 100)


def main():
    lines = sys.stdin.read().splitlines()
    head = lines[0].split() if lines else []
    if len(head) != 2:
        print("error: bad header")
        return
    apr, opening = toi(head[0]), toi(head[1])
    if apr is None or opening is None or not (0 <= apr <= 5000) or not (-1000000 <= opening <= 100000000):
        print("error: bad header")
        return
    charges = payments = 0
    for k in range(1, len(lines)):
        w = lines[k].split()
        if not w:
            continue
        amt = toi(w[1]) if len(w) > 1 else None
        if amt is None or amt < 1 or amt > 100000000 or w[0] not in ("C", "P"):
            print("skipped line %d" % (k + 1))
            continue
        if w[0] == "C":
            charges += amt
        else:
            payments += amt
    interest = (opening * apr + 60000) // 120000 if opening > 0 else 0
    bal = opening + charges - payments + interest
    print("opening: " + money(opening))
    print("charges: " + money(charges))
    print("payments: " + money(payments))
    print("interest: " + money(interest))
    print("new balance: " + money(bal))
    print("minimum payment: " + money(min_payment(bal)))


main()
