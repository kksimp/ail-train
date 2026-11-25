import sys
import re


def main():
    groups = {}
    bad = 0
    for line in sys.stdin.read().splitlines():
        if line == "":
            continue
        f = line.split(" ")
        if (len(f) != 3 or not (f[0].isascii() and f[0].isdigit()) or f[1] == ""
                or not re.fullmatch(r"-?[0-9]+", f[2])):
            bad += 1
            continue
        key = (int(f[0]) // 60 * 60, f[1])
        groups.setdefault(key, []).append(int(f[2]))
    for key in sorted(groups):
        v = groups[key]
        print(f"{key[0]} {key[1]} {len(v)} {sum(v)} {min(v)} {max(v)}")
    print(f"malformed: {bad}")


main()
