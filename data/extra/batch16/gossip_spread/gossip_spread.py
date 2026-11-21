def next_rand(seed):
    seed[0] = (seed[0] * 1103515245 + 12345) % 2147483648
    return seed[0] // 65536

n = 20
informed = [i == 0 for i in range(n)]
seed = [42]
rnd = 0
wasted = 0
while sum(informed) < n and rnd < 30:
    rnd += 1
    senders = [i for i in range(n) if informed[i]]
    fresh = 0
    for s in senders:
        peer = next_rand(seed) % (n - 1)
        if peer >= s:
            peer += 1
        if informed[peer]:
            wasted += 1
        else:
            informed[peer] = True
            fresh += 1
    total = sum(informed)
    bar = "#" * total
    print(f"round {rnd:>2}: +{fresh:<2} {total:>2} {bar}")
print(f"all {n} nodes informed after {rnd} rounds, {wasted} messages hit informed nodes")
