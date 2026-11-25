import sys


def digits(s):
    return s.isascii() and s.isdigit()


def main():
    lines = [l for l in sys.stdin.read().splitlines() if l != ""]
    head = lines[0].split(" ") if lines else []
    if len(head) != 2 or head[0] != "timeout" or not digits(head[1]):
        print("error: bad header")
        return
    limit = int(head[1])
    users = {}
    skipped = 0
    for line in lines[1:]:
        f = line.split(" ")
        if len(f) != 2 or not digits(f[0]) or f[1] == "":
            skipped += 1
            continue
        users.setdefault(f[1], []).append(int(f[0]))
    for u in sorted(users):
        ts = sorted(users[u])
        start = ts[0]
        prev = ts[0]
        n = 1
        for t in ts[1:]:
            if t - prev <= limit:
                n += 1
            else:
                print(f"{u} {start} {prev} {n}")
                start = t
                n = 1
            prev = t
        print(f"{u} {start} {prev} {n}")
    print(f"skipped: {skipped}")


main()
