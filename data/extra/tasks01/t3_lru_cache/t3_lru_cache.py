import sys


def main():
    lines = sys.stdin.read().split("\n")
    if lines[-1] == "":
        lines.pop()
    cap = None
    if lines:
        s = lines[0].strip()
        if s.isascii() and s.isdigit() and int(s) >= 1:
            cap = int(s)
    if cap is None:
        print("bad capacity")
        return
    vals = {}
    order = []  # least recent first
    hits = misses = ev = 0
    for line in lines[1:]:
        w = line.split()
        if not w:
            continue
        c = w[0]
        if c == "put" and len(w) == 3:
            k = w[1]
            if k in vals:
                order.remove(k)
                order.append(k)
                vals[k] = w[2]
                print(f"updated {k}")
            else:
                vals[k] = w[2]
                order.append(k)
                print(f"stored {k}")
                if len(order) > cap:
                    x = order.pop(0)
                    del vals[x]
                    ev += 1
                    print(f"evict {x}")
        elif c == "get" and len(w) == 2:
            k = w[1]
            if k in vals:
                hits += 1
                order.remove(k)
                order.append(k)
                print(vals[k])
            else:
                misses += 1
                print("miss")
        elif c == "peek" and len(w) == 2:
            print(vals.get(w[1], "miss"))
        elif c == "keys" and len(w) == 1:
            print(" ".join(reversed(order)) if order else "(empty)")
        elif c == "stats" and len(w) == 1:
            print(f"hits {hits} misses {misses} evictions {ev}")
        else:
            print("error: bad command")


main()
