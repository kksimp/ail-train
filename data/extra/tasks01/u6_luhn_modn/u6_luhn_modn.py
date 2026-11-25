import sys

ALL = "0123456789abcdefghijklmnopqrstuvwxyz"


def luhn_sum(alpha, s, factor):
    n = len(alpha)
    total = 0
    for c in reversed(s):
        addend = factor * alpha.index(c)
        factor = 1 if factor == 2 else 2
        total += addend // n + addend % n
    return total


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        parts = line.split(" ")
        if parts[0] not in ("gen", "chk") or len(parts) != 3:
            print("bad command")
            continue
        if parts[1] not in ("10", "16", "36"):
            print("error")
            continue
        n = int(parts[1])
        alpha = ALL[:n]
        s = parts[2]
        need = 1 if parts[0] == "gen" else 2
        if len(s) < need or any(c not in alpha for c in s):
            print("error")
            continue
        if parts[0] == "gen":
            total = luhn_sum(alpha, s, 2)
            print(alpha[(n - total % n) % n])
        else:
            print("valid" if luhn_sum(alpha, s, 1) % n == 0 else "invalid")


main()
