rules = ["Saint", "Hawk", "TitForTat", "Grudger", "Alternator", "TitForTwoTats"]
def coop(r, mine, theirs):
    n = len(theirs)
    if r == "Saint": return True
    if r == "Hawk": return False
    if r == "TitForTat": return n == 0 or theirs[n - 1]
    if r == "Grudger": return False not in theirs
    if r == "Alternator": return n % 2 == 0
    return n < 2 or theirs[n - 1] or theirs[n - 2]
def payoff(me, them):
    return 3 if me and them else (0 if me else (5 if them else 1))
def play(a, b):
    ha, hb = [], []
    sa = sb = 0
    for rnd in range(50):
        ca = coop(a, ha, hb)
        cb = coop(b, hb, ha)
        sa += payoff(ca, cb)
        sb += payoff(cb, ca)
        ha.append(ca)
        hb.append(cb)
    return [sa, sb]
totals = [0] * len(rules)
for i in range(len(rules)):
    for j in range(i + 1, len(rules)):
        s = play(rules[i], rules[j])
        totals[i] += s[0]
        totals[j] += s[1]
for i in sorted(range(len(rules)), key=lambda i: (-totals[i], i)):
    print(f"{rules[i]:<14} {totals[i]:>4}")
hd = play("TitForTat", "Hawk")
print(f"tit for tat vs hawk: {hd[0]} to {hd[1]}, it never wins a single match")
