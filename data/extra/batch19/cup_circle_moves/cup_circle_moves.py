def play(labels, total, moves):
    nxt = [0] * (total + 1)
    order = labels + list(range(len(labels) + 1, total + 1))
    for i in range(total):
        nxt[order[i]] = order[(i + 1) % total]
    cur = order[0]
    for _ in range(moves):
        a = nxt[cur]; b = nxt[a]; c = nxt[b]
        nxt[cur] = nxt[c]
        dest = total if cur == 1 else cur - 1
        while dest in (a, b, c):
            dest = total if dest == 1 else dest - 1
        nxt[c] = nxt[dest]; nxt[dest] = a
        cur = nxt[cur]
    return nxt

labels = [int(ch) for ch in "583147926"]
print(f"cups start as {labels}")
small = play(labels, 9, 10)
after = []; v = small[1]
while v != 1:
    after.append(v); v = small[v]
print(f"part 1: after 10 moves, labels after cup 1: {''.join(str(x) for x in after)}")
big = play(labels, 1000, 20000)
x = big[1]; y = big[x]
print(f"part 2: the two cups after cup 1 are {x} and {y}, product {x * y}")
