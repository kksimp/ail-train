import re
import sys

NAMES = ["READ", "WRITE", "EXEC", "HIDDEN", "SYSTEM", "ARCHIVE", "TEMP", "LINK"]


def parse_n(s):
    if not re.fullmatch(r"-?[0-9]{1,12}", s):
        return None, "error number"
    n = int(s)
    if n < 0 or n > 255:
        return None, "error range"
    return n, None


def main():
    for line in sys.stdin.read().split("\n"):
        if line == "":
            continue
        parts = line.split(" ")
        cmd = parts[0]
        args = parts[1:]
        if cmd == "pack":
            v = 0
            err = None
            for a in args:
                if a not in NAMES:
                    err = "error unknown " + a
                    break
                v |= 1 << NAMES.index(a)
            print(err if err else "%d 0x%02x" % (v, v))
        elif cmd == "unpack" and len(args) == 1:
            n, err = parse_n(args[0])
            if err:
                print(err)
            else:
                names = [NAMES[i] for i in range(8) if n >> i & 1]
                print(",".join(names) if names else "none")
        elif cmd in ("toggle", "has") and len(args) == 2:
            n, err = parse_n(args[0])
            if err:
                print(err)
            elif args[1] not in NAMES:
                print("error unknown " + args[1])
            else:
                bit = 1 << NAMES.index(args[1])
                if cmd == "toggle":
                    print(n ^ bit)
                else:
                    print("yes" if n & bit else "no")
        else:
            print("bad command")


main()
