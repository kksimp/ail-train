import re
import sys


def is_int(s):
    return re.fullmatch(r"-?[0-9]+", s) is not None


def main():
    store = {}
    rejected = []
    for n, line in enumerate(sys.stdin.read().splitlines(), 1):
        if line == "":
            continue
        f = line.split(" ", 2)
        cmd = f[0]
        ok = False
        if cmd == "set" and len(f) == 3 and f[1] != "" and f[2] != "":
            store[f[1]] = f[2]
            ok = True
        elif cmd == "del" and len(f) == 2 and f[1] in store:
            del store[f[1]]
            ok = True
        elif cmd == "rename" and len(f) == 3 and f[1] in store and f[2] not in store and f[1] != f[2] and f[2] != "" and " " not in f[2]:
            store[f[2]] = store.pop(f[1])
            ok = True
        elif cmd == "incr" and len(f) == 3 and f[1] != "" and is_int(f[2]) and (f[1] not in store or is_int(store[f[1]])):
            store[f[1]] = str(int(store.get(f[1], "0")) + int(f[2]))
            ok = True
        if not ok:
            rejected.append(n)
    print("state:")
    for k in sorted(store):
        print(f"{k}={store[k]}")
    print(f"rejected: {len(rejected)}")
    for n in rejected:
        print(f"line {n}")


main()
