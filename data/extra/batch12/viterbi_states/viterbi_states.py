states = ["Good", "Worn"]
start = [0.8, 0.2]
trans = [[0.9, 0.1], [0.2, 0.8]]
emit = [[0.6, 0.3, 0.1], [0.1, 0.4, 0.5]]
names = ["Low", "Mid", "High"]
obs = [0, 0, 1, 2, 1, 2, 2, 0]
v = [start[0] * emit[0][obs[0]], start[1] * emit[1][obs[0]]]
back = []
for t in range(1, len(obs)):
    o = obs[t]
    nv = []
    frm = []
    for s in range(2):
        a = v[0] * trans[0][s]
        b = v[1] * trans[1][s]
        if a >= b:
            nv.append(a * emit[s][o])
            frm.append(0)
        else:
            nv.append(b * emit[s][o])
            frm.append(1)
    back.append(frm)
    v = nv
last = 0 if v[0] >= v[1] else 1
best = v[last] * 1000000.0
path = [last]
t = len(back) - 1
while t >= 0:
    last = back[t][last]
    path.append(last)
    t -= 1
path.reverse()
for i in range(len(obs)):
    print(f"Level.{names[obs[i]]}: {states[path[i]]}")
print(f"path likelihood x 10^6: {best:.3f}")
