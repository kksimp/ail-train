import sys


def clean(s):
    return "".join(c for c in s.strip() if c not in " -")


def all_digits(s):
    return all("0" <= c <= "9" for c in s)


def luhn(digits):
    total = 0
    dbl = False
    for ch in reversed(digits):
        v = int(ch)
        if dbl:
            v *= 2
            if v > 9:
                v -= 9
        total += v
        dbl = not dbl
    return total % 10 == 0


def classify(line):
    digits = clean(line)
    n = len(digits)
    if n < 12 or n > 19 or not all_digits(digits):
        return "MALFORMED"
    return "VALID" if luhn(digits) else "INVALID"


def main():
    for line in sys.stdin.read().splitlines():
        t = line.strip()
        if not t:
            continue
        print(f"{t}: {classify(t)}")


main()
