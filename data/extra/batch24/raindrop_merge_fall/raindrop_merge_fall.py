drops = [["a", 20, 1], ["b", 31, 3], ["c", 45, 2], ["d", 52, 5], ["e", 70, 1]]
tick = 0
while drops:
    tick += 1
    for d in drops: d[1] -= 2 + d[2]
    i = 1
    while i < len(drops):
        if drops[i][1] <= drops[i - 1][1]:
            upper = drops.pop(i)
            drops[i - 1][2] += upper[2]
            drops[i - 1][0] = drops[i - 1][0] + upper[0]
            print(f"tick {tick:>2}: {upper[0]} catches up and joins, now {drops[i - 1][0]} of size {drops[i - 1][2]}")
        else:
            i += 1
    while drops and drops[0][1] <= 0:
        gone = drops.pop(0)
        print(f"tick {tick:>2}: {gone[0]} lands with size {gone[2]}")
print(f"all drops down after {tick} ticks")
