state = 5
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
lengths = [4, 7]
scent = [5, 5]
returns = []
window = [0, 0]
for t in range(60):
    for r in returns:
        if r[0] == t: scent[r[1]] += 10
    if t % 5 == 4:
        scent = [v - v // 10 for v in scent]
    trail = 0 if below(scent[0] + scent[1]) < scent[0] else 1
    window[trail] += 1
    returns.append([t + 2 * lengths[trail], trail])
    if t % 10 == 9:
        print(f"minutes {t - 9:>2}-{t:>2}: short {window[0]:>2}, long {window[1]:>2}, scent {scent}")
        window = [0, 0]
trips = [r for r in returns if r[0] < 60]
food = sum(1 for r in trips if r[1] == 0)
print(f"{len(trips)} ants back by minute 60, {food} of them by the short trail")
