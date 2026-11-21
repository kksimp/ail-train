def wiggle_length(xs):
    if len(xs) == 0:
        return 0
    up = 1
    down = 1
    for i in range(1, len(xs)):
        if xs[i] > xs[i - 1]:
            up = down + 1
        elif xs[i] < xs[i - 1]:
            down = up + 1
    return max(up, down)

def turning_points(xs):
    flat = []
    for x in xs:
        if len(flat) == 0 or flat[-1] != x:
            flat.append(x)
    if len(flat) < 3:
        return flat
    out = [flat[0]]
    for i in range(1, len(flat) - 1):
        rising = flat[i] > flat[i - 1]
        falling = flat[i + 1] < flat[i]
        if rising == falling:
            out.append(flat[i])
    out.append(flat[-1])
    return out

for xs in [[1, 7, 4, 9, 2, 5], [1, 17, 5, 10, 13, 15, 10, 5, 16, 8], [1, 2, 3, 4, 5, 6], [3, 3, 3, 3], [10, 22, 9, 33, 49, 50, 31, 60], [5, 1, 1, 6, 2, 2, 8, 0]]:
    run = turning_points(xs)
    print(f"{xs} -> length {wiggle_length(xs)}: {run}")
