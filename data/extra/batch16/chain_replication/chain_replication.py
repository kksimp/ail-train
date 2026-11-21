chain = ["n1", "n2", "n3"]
seq = {"n1": 0, "n2": 0, "n3": 0}
values = ["-", "x=1", "x=2", "x=3", "x=4"]
writes = {1: 1, 2: 2, 4: 3, 6: 4}
acked = 0
for tick in range(1, 11):
    if tick == 5:
        chain = [n for n in chain if n != "n2"]
        print(f"tick  5: n2 fails, chain is now [{', '.join(chain)}]")
    i = len(chain) - 1
    while i > 0:
        up = chain[i - 1]
        me = chain[i]
        if seq[me] < seq[up]:
            seq[me] += 1
        i -= 1
    if tick in writes:
        seq[chain[0]] = writes[tick]
    tail = chain[-1]
    while acked < seq[tail]:
        acked += 1
        print(f"tick {tick:>2}: write {acked} acknowledged")
    positions = " ".join(f"{n}:{seq[n]}" for n in chain)
    print(f"tick {tick:>2}: {positions:<16} read at tail -> {values[seq[tail]]}")
