cot = [("fill", 4), ("wash", 35), ("rinse", 15), ("spin", 10), ("drain", 3)]
tot = sum(m for _, m in cot); t = 0
for n, m in cot:
    print(f"{n:<6} starts at {t:>2} min"); t += m
def run(mi):
    t = 0
    for n, m in cot:
        if mi < t + m: return n
        t += m
    return "done"
for m in [0, 3, 4, 50, 60, 66, 67, 90]:
    print(f"minute {m:>2}: {run(m)}, {max(tot - m, 0)} min left")
