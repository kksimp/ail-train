names = ["white", "yellow", "orange", "red", "blue", "black"]
m = [[0, 10, 15, 20, 25, 30], [40, 0, 10, 15, 30, 25], [45, 35, 0, 10, 28, 22], [50, 40, 30, 0, 20, 15], [45, 38, 35, 25, 0, 12], [60, 55, 50, 45, 35, 0]]

def best(cur, seen):
    if seen == 63:
        return 0
    b = -1
    for nxt in range(6):
        if seen & (1 << nxt) == 0:
            c = m[cur][nxt] + best(nxt, seen | (1 << nxt))
            if b < 0 or c < b:
                b = c
    return b

cur = 0
seen = 1
path = ["white"]
total = best(0, 1)
while seen != 63:
    pick = -1
    for nxt in range(6):
        if seen & (1 << nxt) == 0 and pick == -1:
            if m[cur][nxt] + best(nxt, seen | (1 << nxt)) == best(cur, seen):
                pick = nxt
    print(f"  {names[cur]} -> {names[pick]}: {m[cur][pick]} min")
    path.append(names[pick])
    seen |= 1 << pick
    cur = pick
print(f"best order: {' -> '.join(path)}, {total} minutes")
cur = 0
seen = 1
greedy = 0
gpath = ["white"]
while seen != 63:
    pick = -1
    for nxt in range(6):
        if seen & (1 << nxt) == 0:
            if pick == -1 or m[cur][nxt] < m[cur][pick]:
                pick = nxt
    greedy += m[cur][pick]
    gpath.append(names[pick])
    seen |= 1 << pick
    cur = pick
print(f"nearest next: {' -> '.join(gpath)}, {greedy} minutes")
