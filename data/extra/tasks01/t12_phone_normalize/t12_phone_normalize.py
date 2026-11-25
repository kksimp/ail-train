import sys


def national_digits(t):
    digits = []
    plus = False
    for i, c in enumerate(t):
        if c == "+":
            if i != 0:
                return None
            plus = True
        elif "0" <= c <= "9":
            digits.append(c)
        elif c not in " -.()":
            return None
    d = "".join(digits)
    if plus:
        if len(d) != 11 or not d.startswith("1"):
            return None
        d = d[1:]
    elif len(d) == 11 and d.startswith("1"):
        d = d[1:]
    if len(d) != 10:
        return None
    if d[0] in "01" or d[3] in "01":
        return None
    return d


def normalize(t):
    d = national_digits(t)
    if d is None:
        return "INVALID"
    return f"+1-{d[0:3]}-{d[3:6]}-{d[6:]}"


def main():
    for line in sys.stdin.read().splitlines():
        t = line.strip()
        if not t:
            continue
        print(f"{t} -> {normalize(t)}")


main()
