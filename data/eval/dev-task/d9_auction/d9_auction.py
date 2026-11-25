import sys
import re

lines = sys.stdin.read().splitlines()
if not lines:
    print("no auction")
else:
    reserve, step = (int(x) for x in lines[0].split())
    who = None
    best = 0
    for n, line in enumerate(lines[1:], 2):
        w = line.split()
        if not w:
            continue
        if len(w) != 2 or not re.fullmatch(r"-?[0-9]+", w[1]) or int(w[1]) <= 0:
            print(f"line {n}: malformed")
            continue
        name, amount = w[0], int(w[1])
        need = reserve if who is None else best + step
        if amount >= need and name != who:
            who, best = name, amount
            print(f"{name} {amount} accepted")
        else:
            print(f"{name} {amount} rejected")
    if who is None:
        print("no sale")
    else:
        print(f"winner {who} at {best}")
