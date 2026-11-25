import re
import sys


def num(tok):
    return int(tok) if re.fullmatch(r"[0-9]+", tok) else 0


queue = []      # [id, prio, pages], in submission order
current = None  # [id, prio, pages]
seen = set()
finished = 0
cancelled = 0


def by_priority():
    return sorted(queue, key=lambda j: -j[1])


for n, raw in enumerate(sys.stdin.read().splitlines(), 1):
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    w = line.split()
    cmd = w[0]
    if cmd == "submit":
        if len(w) != 4:
            print(f"error line {n}: bad arguments")
            continue
        prio = num(w[2])
        pages = num(w[3])
        if prio < 1 or prio > 9:
            print(f"error line {n}: bad priority")
        elif pages < 1:
            print(f"error line {n}: bad pages")
        elif w[1] in seen:
            print(f"error line {n}: duplicate job {w[1]}")
        else:
            seen.add(w[1])
            queue.append([w[1], prio, pages])
    elif cmd == "cancel":
        if len(w) != 2:
            print(f"error line {n}: bad arguments")
            continue
        jid = w[1]
        if current is not None and current[0] == jid:
            current = None
            cancelled += 1
            print(f"cancelled {jid} (printing)")
        elif any(j[0] == jid for j in queue):
            queue = [j for j in queue if j[0] != jid]
            cancelled += 1
            print(f"cancelled {jid}")
        elif jid in seen:
            print(f"error line {n}: job {jid} not active")
        else:
            print(f"error line {n}: unknown job {jid}")
    elif cmd == "tick":
        if len(w) != 1:
            print(f"error line {n}: bad arguments")
            continue
        budget = 10
        while budget > 0:
            if current is None:
                if not queue:
                    break
                best = by_priority()[0]
                queue.remove(best)
                current = best
                print(f"  start {best[0]}")
            used = min(budget, current[2])
            current[2] -= used
            budget -= used
            if current[2] == 0:
                print(f"  done {current[0]}")
                current = None
                finished += 1
        print(f"tick: {10 - budget} pages")
    elif cmd == "status":
        if len(w) != 1:
            print(f"error line {n}: bad arguments")
            continue
        if current is None:
            print("printing: none")
        else:
            print(f"printing: {current[0]} ({current[2]} left)")
        items = [f"{j[0]}:{j[1]}:{j[2]}" for j in by_priority()]
        print("queued: " + (" ".join(items) if items else "none"))
        print(f"finished {finished} cancelled {cancelled}")
    else:
        print(f"error line {n}: unknown command")
pending = len(queue) + (1 if current is not None else 0)
print(f"summary: finished {finished} cancelled {cancelled} pending {pending}")
