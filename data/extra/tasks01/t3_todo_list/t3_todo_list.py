import sys


def main():
    items = []  # [id, text, done]
    nxt = 1
    lines = sys.stdin.read().split("\n")
    for line in lines:
        if line.strip() == "":
            continue
        p = line.split(" ", 1)
        c = p[0]
        if c == "add" and len(p) == 2 and p[1] != "":
            items.append([nxt, p[1], False])
            print(f"added {nxt}")
            nxt += 1
        elif c in ("done", "undo", "rm") and len(p) == 2 and p[1].isascii() and p[1].isdigit() and int(p[1]) >= 1:
            i = int(p[1])
            it = next((x for x in items if x[0] == i), None)
            if it is None:
                print(f"error: no item {i}")
            elif c == "rm":
                items.remove(it)
                print(f"removed {i}")
            else:
                it[2] = c == "done"
                print(f"{i} done" if it[2] else f"{i} open")
        elif c in ("list", "open") and len(p) == 1:
            rows = [x for x in items if c == "list" or not x[2]]
            if not rows:
                print("(empty)" if c == "list" else "(none open)")
            for x in rows:
                print(f"[{'x' if x[2] else ' '}] {x[0]} {x[1]}")
        elif c == "clear" and len(p) == 1:
            n = sum(1 for x in items if x[2])
            items = [x for x in items if not x[2]]
            print(f"cleared {n}")
        elif c == "count" and len(p) == 1:
            d = sum(1 for x in items if x[2])
            print(f"open {len(items) - d} done {d}")
        else:
            print("error: bad command")


main()
