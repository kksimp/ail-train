import math
def mean(xs):
    t = 0.0
    for x in xs:
        t = t + x
    return t / float(len(xs))
def stdev(xs):
    m = mean(xs)
    ss = 0.0
    for x in xs:
        ss = ss + (x - m) * (x - m)
    return math.sqrt(ss / float(len(xs) - 1))
rf = 0.25
twelve = 12.0
funds = {"steady bond": [0.4, 0.3, 0.5, 0.4, 0.2, 0.4, 0.3, 0.5, 0.4, 0.3, 0.4, 0.5], "global shares": [2.1, -1.5, 3.0, 0.8, -2.2, 1.9, 2.5, -0.7, 1.2, 0.4, -1.1, 2.8], "tech growth": [5.2, -4.8, 6.1, -3.0, 4.4, -5.5, 7.0, 1.0, -2.5, 3.8, -6.0, 6.5]}
best = ""
best_s = -100.0
for name, rets in funds.items():
    m = mean(rets)
    sd = stdev(rets)
    sharpe = (m - rf) / sd * math.sqrt(twelve)
    print(f"{name:<13} mean {m:>5.2f}% a month, sd {sd:>5.2f}%, Sharpe {sharpe:>5.2f}")
    if sharpe > best_s:
        best = name
        best_s = sharpe
print(f"best reward for risk: {best}")
