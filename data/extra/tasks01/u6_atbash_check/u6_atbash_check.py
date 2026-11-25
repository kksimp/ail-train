import sys


def atbash(c):
    if "A" <= c <= "Z":
        return chr(155 - ord(c))
    if "a" <= c <= "z":
        return chr(219 - ord(c))
    return c


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        text = "".join(atbash(c) for c in line)
        count = 0
        total = 0
        for c in text:
            if ("A" <= c <= "Z") or ("a" <= c <= "z"):
                count += 1
                total += (ord(c.upper()) - 64) * count
        print("%s|%d|%d" % (text, count, total % 97))


main()
