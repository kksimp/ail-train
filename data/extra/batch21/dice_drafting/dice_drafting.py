def next_state(s):
    return (s * 1103515245 + 12345) % 2147483648

def pairs(xs):
    return sum(xs.count(v) // 2 for v in range(1, 7))

def choose(pool, mine, chase):
    best = 0
    for i, d in enumerate(pool):
        if d > pool[best]:
            best = i
    if chase:
        pair = -1
        for i, d in enumerate(pool):
            if d in mine and (pair < 0 or d > pool[pair]):
                pair = i
        if pair >= 0:
            return pair
    return best

def show(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"

names = ["High", "Pairs"]
s = 99
totals = [0, 0]
for r in range(4):
    pool = []
    for k in range(6):
        s = next_state(s)
        pool.append((s >> 16) % 6 + 1)
    rolled = sorted(pool)
    picks = [[], []]
    who = r % 2
    while pool:
        i = choose(pool, picks[who], who == 1)
        picks[who].append(pool[i])
        pool.pop(i)
        who = 1 - who
    line = []
    for p in range(2):
        pts = sum(picks[p]) + 5 * pairs(picks[p])
        totals[p] += pts
        line.append(f"{names[p]} {show(picks[p])} = {pts}")
    print(f"round {r + 1}: rolled {show(rolled)}; {', '.join(line)}")
print(f"totals: High {totals[0]}, Pairs {totals[1]}")
