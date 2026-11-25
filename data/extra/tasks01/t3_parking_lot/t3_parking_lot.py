import sys


def num(s):
    if s.isascii() and s.isdigit():
        return int(s)
    return None


def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    h = lines[0].split() if lines else []
    n = num(h[1]) if len(h) == 2 and h[0] == "capacity" else None
    if n is None or not 1 <= n <= 99:
        print("bad header")
        return
    spots = [None] * (n + 1)  # spot -> (plate, time)
    revenue = 0
    for line in lines[1:]:
        w = line.split()
        if not w:
            continue
        c = w[0]
        if c == "status" and len(w) == 1:
            occ = [(i, spots[i]) for i in range(1, n + 1) if spots[i]]
            print(f"free {n - len(occ)} of {n}")
            for i, (p, _) in occ:
                print(f"{i} {p}")
            continue
        t = num(w[1]) if len(w) == 3 and c in ("park", "leave") else None
        if t is None:
            print("error: bad command")
            continue
        plate = w[2]
        cur = next((i for i in range(1, n + 1) if spots[i] and spots[i][0] == plate), None)
        if c == "park":
            if cur is not None:
                print(f"error: already parked {plate}")
                continue
            free = next((i for i in range(1, n + 1) if not spots[i]), None)
            if free is None:
                print(f"{plate} rejected: full")
            else:
                spots[free] = (plate, t)
                print(f"{plate} spot {free}")
        else:
            if cur is None:
                print(f"error: not parked {plate}")
                continue
            dur = t - spots[cur][1]
            if dur < 0:
                print("error: time went backwards")
                continue
            fee = 2 * max(1, (dur + 59) // 60)
            revenue += fee
            spots[cur] = None
            print(f"{plate} left spot {cur} fee {fee}")
    print(f"revenue {revenue}")
    print(f"occupied {sum(1 for i in range(1, n + 1) if spots[i])}")


main()
