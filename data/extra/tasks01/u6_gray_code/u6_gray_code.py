import sys


def parse_num(s):
    if not (1 <= len(s) <= 10 and all(c in "0123456789" for c in s)):
        return None
    n = int(s)
    return n if n <= 4294967295 else None


def parse_bits(s):
    if not (1 <= len(s) <= 32 and all(c in "01" for c in s)):
        return None
    return int(s, 2)


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        parts = line.split(" ")
        cmd = parts[0]
        if len(parts) != 2 or cmd not in ("bin", "dec", "gray", "ungray"):
            print("bad command")
            continue
        arg = parts[1]
        if cmd in ("bin", "gray"):
            n = parse_num(arg)
            if n is None:
                print("error")
            elif cmd == "bin":
                print(format(n, "b"))
            else:
                print(format(n ^ (n >> 1), "b"))
        else:
            v = parse_bits(arg)
            if v is None:
                print("error")
            elif cmd == "dec":
                print(v)
            else:
                n = v
                s = v >> 1
                while s:
                    n ^= s
                    s >>= 1
                print(n)


main()
