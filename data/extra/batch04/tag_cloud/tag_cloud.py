P = [["ail", "compilers", "speed"], ["ail", "testing"], ["gardening"], ["ail", "speed", "benchmarks"], ["compilers", "ail"], ["testing", "speed"], ["ail"]]
c = {}
for p in P:
    for t in p: c[t] = c.get(t, 0) + 1
b = max(c.values())
for t in sorted(c): print(f"{t:<11} {c[t]} {'*' * (1 + (c[t] - 1) * 4 // max(b - 1, 1))}")
