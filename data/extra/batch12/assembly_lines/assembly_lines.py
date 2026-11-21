work = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
hop = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
enter = [2, 4]
leave = [3, 2]
n = len(work[0])
best = [[enter[0] + work[0][0]], [enter[1] + work[1][0]]]
came = [[0], [1]]
for s in range(1, n):
    for line in range(2):
        other = 1 - line
        stay = best[line][s - 1] + work[line][s]
        cross = best[other][s - 1] + hop[other][s - 1] + work[line][s]
        if stay <= cross:
            best[line].append(stay)
            came[line].append(line)
        else:
            best[line].append(cross)
            came[line].append(other)
a = best[0][n - 1] + leave[0]
b = best[1][n - 1] + leave[1]
line = 0 if a <= b else 1
total = min(a, b)
route = [line]
s = n - 1
while s > 0:
    line = came[line][s]
    route.append(line)
    s -= 1
route.reverse()
print(f"line 1 times: {best[0]}")
print(f"line 2 times: {best[1]}")
print(f"stations use lines {' '.join(str(l + 1) for l in route)}")
print(f"finished in {total} minutes")
