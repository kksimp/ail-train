def rebalance(banks):
    n = len(banks); top = 0
    for i in range(1, n):
        if banks[i] > banks[top]: top = i
    blocks = banks[top]; banks[top] = 0; i = top
    while blocks > 0:
        i = (i + 1) % n; banks[i] += 1; blocks -= 1

banks = [3, 0, 7, 2, 5, 1]
print(f"start: {banks}")
seen = {}; rounds = 0
while ",".join(map(str, banks)) not in seen:
    seen[",".join(map(str, banks))] = rounds
    rebalance(banks); rounds += 1
    if rounds <= 3:
        print(f"round {rounds}: {banks}")
first = seen[",".join(map(str, banks))]
print(f"repeated layout: {banks}")
print(f"part 1: a layout repeats after {rounds} rounds")
print(f"part 2: the loop is {rounds - first} rounds long")
