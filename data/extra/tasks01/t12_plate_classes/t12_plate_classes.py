import sys


def shape_char(c):
    if "A" <= c <= "Z":
        return "L"
    if "0" <= c <= "9":
        return "D"
    return c


def shape_of(plate):
    return "".join(shape_char(c) for c in plate)


def is_vanity(shape):
    n = len(shape)
    if n < 2 or n > 7:
        return False
    return shape.startswith("L") and all(c in "LD" for c in shape)


def classify(plate):
    shape = shape_of(plate)
    if shape == "LLL-DDD":
        return "classic"
    if shape == "LL-DD-LL":
        return "euro"
    if shape == "DLLLDDD":
        return "californian"
    if is_vanity(shape):
        return "vanity"
    return "invalid"


def main():
    for line in sys.stdin.read().splitlines():
        t = line.strip()
        if not t:
            continue
        print(f"{t}: {classify(t)}")


main()
