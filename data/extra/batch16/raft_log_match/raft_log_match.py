def sync(leader, follower):
    nxt = len(leader) + 1
    rounds = 0
    while True:
        rounds += 1
        prev = nxt - 1
        prev_term = 0 if prev == 0 else leader[prev - 1]
        has = prev == 0 or (prev <= len(follower) and follower[prev - 1] == prev_term)
        if not has:
            print(f"  prev index {prev} term {prev_term}: rejected")
            nxt -= 1
            continue
        cut = -1
        for idx in range(nxt, len(leader) + 1):
            if cut < 0 and idx <= len(follower) and follower[idx - 1] != leader[idx - 1]:
                cut = idx
        if cut > 0:
            del follower[cut - 1:]
        for idx in range(len(follower) + 1, len(leader) + 1):
            follower.append(leader[idx - 1])
        note = f"replaced from index {cut}" if cut > 0 else "nothing to replace"
        print(f"  prev index {prev} term {prev_term}: accepted, {note}")
        break
    return rounds

leader = [1, 1, 1, 2, 3, 3, 3]
print(f"leader log {leader}")
for start in [[1, 1, 1, 2, 2, 2], [1, 1], [1, 1, 1, 2, 3]]:
    f = list(start)
    print(f"follower {start}:")
    rounds = sync(leader, f)
    same = "matches leader" if f == leader else "differs"
    print(f"  after {rounds} messages: {f} {same}")
