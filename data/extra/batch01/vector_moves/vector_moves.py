pos = [0, 0]; done = []
for m in ["3,1", "-2, 4", "oops", "0,-6", "5,5"]:
    p = m.split(",")
    try:
        if len(p) != 2: raise ValueError
        v = (int(p[0].strip()), int(p[1].strip()))
    except ValueError:
        print(f"skip '{m}'"); continue
    pos[0] += v[0]; pos[1] += v[1]; done.append(v)
    print(f"after {m}: ({pos[0]}, {pos[1]})")
b = list(pos)
for v in reversed(done):
    b[0] -= v[0]; b[1] -= v[1]
print(f"walked back to ({b[0]}, {b[1]})")
print(f"from (10, 10): ({pos[0] - 10}, {pos[1] - 10})")
