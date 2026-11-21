def clock(m):
    return f"{m // 60:02d}:{m % 60:02d}"

def check(order, travel, opens, closes):
    t = 480
    at = 0
    late = 0
    for s in order:
        t += travel[at][s]
        arrive = t
        if t < opens[s]:
            t = opens[s]
        state = "late" if arrive > closes[s] else ("waits" if arrive < opens[s] else "on time")
        if arrive > closes[s]:
            late += 1
        print(f"  stop {s}: arrive {clock(arrive)}, window {clock(opens[s])}-{clock(closes[s])}, {state}")
        t += 10
        at = s
    t += travel[at][0]
    print(f"  back at depot {clock(t)}, {late} late")
    return late

travel = [[0, 20, 25, 15, 30], [20, 0, 10, 18, 22], [25, 10, 0, 20, 15], [15, 18, 20, 0, 28], [30, 22, 15, 28, 0]]
opens = [0, 510, 540, 480, 600]
closes = [0, 570, 600, 540, 660]
print("order 1-2-3-4:")
a = check([1, 2, 3, 4], travel, opens, closes)
print("order 3-1-2-4:")
b = check([3, 1, 2, 4], travel, opens, closes)
best = "3-1-2-4" if b < a else "1-2-3-4"
print(f"use {best}")
