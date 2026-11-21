def simulate(cs, ts, horizon, edf):
    n = len(cs)
    left = [0] * n
    due = [0] * n
    line = []
    misses = 0
    for t in range(horizon):
        for i in range(n):
            if t % ts[i] == 0:
                if left[i] > 0:
                    misses += 1
                left[i] = cs[i]
                due[i] = t + ts[i]
        pick = -1
        for i in range(n):
            if left[i] > 0:
                if pick < 0 or (due[i] < due[pick] if edf else ts[i] < ts[pick]):
                    pick = i
        if pick < 0:
            line.append(".")
        else:
            left[pick] -= 1
            line.append(["A", "B", "C"][pick])
    return f"{''.join(line)}  misses {misses}"

cs = [1, 2, 3]
ts = [4, 6, 8]
print("tasks A 1/4, B 2/6, C 3/8; horizon 24")
print(f"EDF: {simulate(cs, ts, 24, True)}")
print(f"RM:  {simulate(cs, ts, 24, False)}")
