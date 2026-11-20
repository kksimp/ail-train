arr = [(0, 12), (0, 3), (1, 20), (1, 7), (2, 4), (3, 9), (5, 15), (6, 2)]
L = 3; load = [0] * L; sa = [0] * L; minute = nxt = 0
while nxt < len(arr) or any(load):
    while nxt < len(arr) and arr[nxt][0] == minute:
        it = arr[nxt][1]; b = 0
        for i in range(1, L):
            if load[i] < load[b]: b = i
        load[b] += it
        print(f"t{minute}: shopper {nxt + 1} ({it} items) -> lane {b + 1}"); nxt += 1
    for i in range(L):
        if load[i] > 0:
            load[i] = max(load[i] - 5, 0)
            if load[i] == 0: sa[i] = minute + 1
    minute += 1
print("lanes last empty at: " + " ".join(f"t{t}" for t in sa))
print(f"total minutes: {minute}")
