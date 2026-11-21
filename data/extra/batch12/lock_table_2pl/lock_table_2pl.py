def compatible(held, r):
    for h in held:
        if h[2] == r[2] and h[0] != r[0] and (h[1] == "X" or r[1] == "X"):
            return False
    return True

script = [(1, "S", "acct"), (2, "S", "acct"), (3, "X", "acct"), (2, "X", "loan"), (1, "X", "loan"), (2, "commit", ""), (1, "commit", ""), (3, "commit", "")]
held = []
waiting = []
for tx, mode, item in script:
    if mode == "commit":
        held = [h for h in held if h[0] != tx]
        print(f"T{tx} commits, releases its locks")
        blocked_now = []
        for w in waiting:
            if compatible(held, w):
                held.append(w)
                print(f"  T{w[0]} wakes, gets {w[1]} on {w[2]}")
            else:
                blocked_now.append(w)
        waiting = blocked_now
        continue
    r = (tx, mode, item)
    if any(w[0] == tx for w in waiting):
        print(f"T{tx} is blocked, request queued behind its wait")
        waiting.append(r)
    elif compatible(held, r):
        held.append(r)
        print(f"T{tx} gets {mode} on {item}")
    else:
        waiting.append(r)
        print(f"T{tx} waits for {mode} on {item}")
print(f"locks held at the end: {len(held)}, waiting: {len(waiting)}")
