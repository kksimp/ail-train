def blocking(a, c):
    b = 1.0
    for k in range(1, c + 1):
        b = a * b / (float(k) + a * b)
    return b
a = 5.0
for c in range(1, 11):
    print(f"{c:>2} lines for 5 erlangs: {blocking(a, c) * 100.0:>6.2f}% of calls blocked")
for load in [1.0, 3.0, 8.0, 20.0]:
    c = 1
    while blocking(load, c) >= 0.01:
        c += 1
    print(f"{load} erlangs need {c} lines for under 1% blocking ({blocking(load, c) * 100.0:.2f}%)")
