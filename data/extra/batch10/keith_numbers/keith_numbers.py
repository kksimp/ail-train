def keith_run(n):
    seq = [int(c) for c in str(n)]
    d = len(seq)
    while seq[-1] < n:
        seq.append(sum(seq[-d:]))
    return seq

def is_keith(n):
    return n >= 10 and keith_run(n)[-1] == n

found = [n for n in range(10, 100000) if is_keith(n)]
print(f"{len(found)} Keith numbers below 100000:")
for i in range(0, len(found), 8):
    print(f"  {found[i:i + 8]}")
for n in [197, 742, 7385, 198]:
    run = keith_run(n)
    verdict = "Keith" if run[-1] == n else "not Keith"
    print(f"{n}: {run} -> {verdict}")
