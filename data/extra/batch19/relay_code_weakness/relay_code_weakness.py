def valid(xs, i, width):
    for a in range(i - width, i):
        for b in range(a + 1, i):
            if xs[a] != xs[b] and xs[a] + xs[b] == xs[i]:
                return True
    return False

stream = [20, 7, 13, 4, 11, 24, 18, 17, 22, 29, 35, 40, 53, 31, 75, 66, 81]
width = 5; bad = -1
for i in range(width, len(stream)):
    if not valid(stream, i, width):
        bad = stream[i]
        print(f"part 1: {bad} at position {i} is not a sum of two of the previous {width}")
        break
for start in range(len(stream)):
    total = 0; stop = start
    while total < bad and stop < len(stream):
        total += stream[stop]; stop += 1
    if total == bad and stop - start >= 2:
        run = stream[start:stop]
        print(f"run {run} sums to {bad}")
        print(f"part 2: {min(run)} + {max(run)} = {min(run) + max(run)}")
        break
