S = ["Ada", "Bo", "Cal", "Dot", "Eli"]; J = ["fire", "water", "cook", "wash", "rest"]; D = {s: [] for s in S}
for d in range(5):
    ln = []
    for i, s in enumerate(S): j = J[(i + d * 2) % 5]; D[s].append(j); ln.append(f"{s}:{j}")
    print(f"day {d + 1}: {' '.join(ln)}")
for s in S: print(f"{s} did every job: {'true' if sorted(D[s]) == sorted(J) else 'false'}")
