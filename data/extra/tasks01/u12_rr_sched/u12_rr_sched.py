import sys
from collections import deque

lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
q = 0
if lines:
    f = lines[0].split()
    if len(f) == 2 and f[0] == "quantum":
        try:
            q = int(f[1])
        except ValueError:
            q = 0
if q < 1:
    print("bad quantum")
    sys.exit(0)
procs = []
bad = 0
for l in lines[1:]:
    f = l.split()
    try:
        if len(f) != 3:
            raise ValueError
        a, b = int(f[1]), int(f[2])
        if a < 0 or b < 1:
            raise ValueError
        procs.append((f[0], a, b))
    except ValueError:
        bad += 1
n = len(procs)
order = sorted(range(n), key=lambda i: procs[i][1])
rem = [p[2] for p in procs]
fin = [0] * n
t = 0
nxt = 0
dq = deque()
slices = []
while True:
    if not dq:
        if nxt == n:
            break
        t = max(t, procs[order[nxt]][1])
    while nxt < n and procs[order[nxt]][1] <= t:
        dq.append(order[nxt]); nxt += 1
    i = dq.popleft()
    run = min(q, rem[i])
    slices.append(f"{t}-{t+run} {procs[i][0]}")
    t += run
    rem[i] -= run
    while nxt < n and procs[order[nxt]][1] <= t:
        dq.append(order[nxt]); nxt += 1
    if rem[i] > 0:
        dq.append(i)
    else:
        fin[i] = t
out = slices
for i in range(n):
    name, a, b = procs[i]
    ta = fin[i] - a
    out.append(f"{name} finish={fin[i]} turnaround={ta} wait={ta-b}")
out.append(f"ignored {bad}")
print("\n".join(out))
