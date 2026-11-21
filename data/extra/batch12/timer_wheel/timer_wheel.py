slots = 8
wheel = [[] for _ in range(slots)]
starts = [("retry", 3), ("heartbeat", 5), ("session", 19), ("flush", 8), ("lease", 11), ("probe", 3), ("audit", 27)]
for name, delay in starts:
    wheel[delay % slots].append((name, (delay - 1) // slots))
    print(f"set {name:<9} for tick {delay:>2}: slot {delay % slots}, {(delay - 1) // slots} turns")
checked = 0
for tick in range(1, 29):
    slot = tick % slots
    keep = []
    for name, rounds in wheel[slot]:
        checked += 1
        if rounds == 0:
            print(f"tick {tick:>2}: {name} fires")
        else:
            keep.append((name, rounds - 1))
    wheel[slot] = keep
print(f"{checked} timer checks over 28 ticks")
