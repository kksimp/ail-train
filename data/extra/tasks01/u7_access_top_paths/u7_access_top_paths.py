import sys


def all_digits(s):
    return s.isascii() and s.isdigit()


def main():
    counts = {}
    classes = [0] * 5
    bad = 0
    for line in sys.stdin.read().splitlines():
        if line == "":
            continue
        f = line.split(" ")
        if len(f) != 5 or any(x == "" for x in f) or not all_digits(f[3]) or not all_digits(f[4]):
            bad += 1
            continue
        status = int(f[3])
        if status < 100 or status > 599:
            bad += 1
            continue
        counts[f[2]] = counts.get(f[2], 0) + 1
        classes[status // 100 - 1] += 1
    print("top paths:")
    for c, p in sorted((-c, p) for p, c in counts.items())[:3]:
        print(f"{-c} {p}")
    print("status:")
    for i in range(5):
        print(f"{i + 1}xx {classes[i]}")
    print(f"malformed: {bad}")


main()
