import sys


def all_digits(s):
    return all("0" <= c <= "9" for c in s)


def part_problem(p):
    if p == "":
        return "empty part"
    if not all_digits(p):
        return "non-digit"
    if len(p) > 1 and p.startswith("0"):
        return "leading zero"
    if len(p) > 3:
        return "out of range"
    if int(p) > 255:
        return "out of range"
    return None


def classify(o):
    a, b = o[0], o[1]
    if a == 127:
        return "loopback"
    if a == 10 or (a == 172 and 16 <= b <= 31) or (a == 192 and b == 168):
        return "private"
    if a == 169 and b == 254:
        return "link-local"
    if 224 <= a <= 239:
        return "multicast"
    if all(x == 0 for x in o):
        return "unspecified"
    return "public"


def check(line):
    parts = line.split(".")
    if len(parts) != 4:
        return "invalid (wrong part count)"
    for p in parts:
        why = part_problem(p)
        if why is not None:
            return f"invalid ({why})"
    return "valid " + classify([int(p) for p in parts])


def main():
    for line in sys.stdin.read().splitlines():
        t = line.strip()
        if not t:
            continue
        print(f"{t}: {check(t)}")


main()
