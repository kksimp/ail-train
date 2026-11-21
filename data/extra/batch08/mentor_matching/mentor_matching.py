st = ["Ava", "Ben", "Cia", "Dan"]; me = ["Ng", "Ortiz", "Patel", "Quinn"]
wants = [[0, 1, 2, 3], [0, 2, 1, 3], [1, 0, 3, 2], [0, 3, 2, 1]]
likes = [[1, 0, 3, 2], [2, 0, 1, 3], [3, 2, 0, 1], [0, 1, 2, 3]]
rank = []
for m in range(4):
    row = [0] * 4
    for pos in range(4): row[likes[m][pos]] = pos
    rank.append(row)
partner = [-1] * 4; tried = [0] * 4; queue = [0, 1, 2, 3]; head = 0
while head < len(queue):
    s = queue[head]; head += 1; m = wants[s][tried[s]]; tried[s] += 1; cur = partner[m]
    if cur == -1: partner[m] = s; print(f"{st[s]} asks {me[m]}: yes")
    elif rank[m][s] < rank[m][cur]: partner[m] = s; queue.append(cur); print(f"{st[s]} asks {me[m]}: yes, {st[cur]} is free again")
    else: queue.append(s); print(f"{st[s]} asks {me[m]}: no")
for m in range(4): print(f"{me[m]} mentors {st[partner[m]]}")
