ws = [3, 5, 9, 14, 20]; T = sum(ws)
can = [False] * (T + 1); can[0] = True
for w in ws:
    for t in range(T, w - 1, -1):
        if can[t - w]: can[t] = True
print(f"totals 0..{T}: {sum(can)} reachable")
print(f"cannot make: {[t for t in range(T + 1) if not can[t]][:12]}")
def fs(ws, t):
    if t == 0: return []
    if not ws or t < 0: return None
    r = fs(ws[1:], t - ws[0])
    if r is not None: return [ws[0]] + r
    return fs(ws[1:], t)
for t in [17, 26, 30, 50, 4]:
    s = fs(ws, t)
    print(f"{t} = {' + '.join(map(str, s))}" if s is not None else f"{t}: impossible")
