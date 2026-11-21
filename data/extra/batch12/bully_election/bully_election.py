def elect(start, alive, msgs, log):
    n = len(alive)
    answered = False
    for h in range(start + 1, n):
        msgs[0] += 1
        if alive[h]:
            msgs[0] += 1
            answered = True
            log.append(f"n{start} -> n{h}: election, n{h} answers ok")
    if not answered:
        return start
    up = n - 1
    while not alive[up]:
        up -= 1
    if up == start:
        return start
    nxt = start + 1
    while not alive[nxt]:
        nxt += 1
    return elect(nxt, alive, msgs, log)

alive = [True] * 6
alive[5] = False
alive[4] = False
msgs = [0]
log = []
leader = elect(1, alive, msgs, log)
for line in log:
    print(line)
print(f"n{leader} announces itself coordinator to {sum(1 for a in alive if a) - 1} nodes")
print(f"{msgs[0]} election messages")
alive[4] = True
msgs2 = [0]
log2 = []
again = elect(3, alive, msgs2, log2)
print(f"n4 restarts: n3 notices, n{again} wins after {msgs2[0]} messages")
