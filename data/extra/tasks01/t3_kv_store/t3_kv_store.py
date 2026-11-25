import sys


def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    db = {}
    for line in lines:
        if line == "":
            continue
        p = line.split(" ", 2)
        c = p[0]
        n = len(line.split(" "))
        if c == "set" and len(p) == 3 and p[1] != "" and p[2] != "":
            db[p[1]] = p[2]
            print("ok")
        elif c in ("get", "del", "incr") and n == 2 and p[1] != "":
            k = p[1]
            if c == "get":
                print(db.get(k, "(nil)"))
            elif c == "del":
                if k in db:
                    del db[k]
                    print("deleted")
                else:
                    print("missing")
            else:
                v = db.get(k, "0")
                if v.isascii() and v.lstrip("-").isdigit() and v != "-":
                    db[k] = str(int(v) + 1)
                    print(db[k])
                else:
                    print("error: not an integer")
        elif c == "count" and n == 1:
            print(len(db))
        elif c == "keys" and n == 1:
            print(" ".join(sorted(db)) if db else "(empty)")
        else:
            print("error: bad command")


main()
