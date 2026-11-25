import sys


def order(length, n):
    cycle = 2 * (n - 1)

    def rail(i):
        r = i % cycle
        return r if r < n else cycle - r

    out = []
    for k in range(n):
        for i in range(length):
            if rail(i) == k:
                out.append(i)
    return out


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        parts = line.split(" ", 2)
        if len(parts) < 2 or parts[0] not in ("E", "D"):
            print("bad command")
            continue
        s = parts[1]
        if not (s.isascii() and (s.isdigit() or (s[:1] == "-" and s[1:].isdigit()))):
            print("bad rails")
            continue
        n = int(s)
        if n < 2 or n > 10:
            print("bad rails")
            continue
        text = parts[2] if len(parts) > 2 else ""
        idx = order(len(text), n)
        if parts[0] == "E":
            print("".join(text[i] for i in idx))
        else:
            res = [""] * len(text)
            for j, i in enumerate(idx):
                res[i] = text[j]
            print("".join(res))


main()
