def steps(s):
    t = str(s).zfill(4)
    if len(set(t)) == 1:
        return None
    seq, v = [s], s
    while v != 6174:
        d = sorted(str(v).zfill(4))
        v = int("".join(reversed(d))) - int("".join(d))
        seq.append(v)
        if len(seq) > 10:
            return None
    return seq
for n in [3524, 2111, 9831, 6174, 1000, 7777]:
    s = steps(n)
    if s:
        print(f"{n}: {len(s) - 1} steps (" + " -> ".join(str(x).zfill(4) for x in s) + ")")
    else:
        print(f"{n}: all digits equal")
most = max(len(steps(n) or []) for n in range(1000, 10000))
print(f"longest: {most - 1} steps")
