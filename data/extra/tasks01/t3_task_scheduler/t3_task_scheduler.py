import sys


def num(s):
    if s.isascii() and s.lstrip("-").isdigit() and s != "-":
        return int(s)
    return None


def order(tasks):
    return sorted(tasks, key=lambda t: (-t[1], t[2]))


def main():
    tasks = []  # [name, prio, seq]
    seq = 0
    for line in sys.stdin.read().split("\n"):
        w = line.split()
        if not w:
            continue
        c = w[0]
        want = {"add": 3, "next": 1, "bump": 3, "cancel": 2, "list": 1}
        if c not in want or len(w) != want[c]:
            print("error: bad command")
            continue
        if c == "add":
            p = num(w[2])
            if p is None or not 1 <= p <= 9:
                print("error: bad priority")
            elif any(t[0] == w[1] for t in tasks):
                print(f"error: duplicate {w[1]}")
            else:
                seq += 1
                tasks.append([w[1], p, seq])
                print(f"added {w[1]}")
        elif c == "next":
            if not tasks:
                print("idle")
            else:
                t = order(tasks)[0]
                tasks.remove(t)
                print(f"run {t[0]} {t[1]}")
        elif c == "bump":
            n = num(w[2])
            if n is None or n < 1:
                print("error: bad priority")
                continue
            for t in tasks:
                if t[0] == w[1]:
                    t[1] = min(9, t[1] + n)
                    print(f"{t[0]} now {t[1]}")
                    break
            else:
                print(f"error: no such task {w[1]}")
        elif c == "cancel":
            for t in tasks:
                if t[0] == w[1]:
                    tasks.remove(t)
                    print(f"cancelled {w[1]}")
                    break
            else:
                print(f"error: no such task {w[1]}")
        else:
            if not tasks:
                print("empty")
            for t in order(tasks):
                print(f"{t[0]}:{t[1]}")


main()
