jobs = [("A", 7), ("B", 5), ("C", 4), ("D", 3), ("E", 3), ("F", 2), ("G", 6)]
order = sorted(jobs, key=lambda j: -j[1])
loads = [0, 0, 0]
rows = ["", "", ""]
for name, time in order:
    m = 0
    for i in range(1, 3):
        if loads[i] < loads[m]:
            m = i
    rows[m] += name * time
    loads[m] += time
span = max(loads)
axis = "".join(str(t % 10) for t in range(span))
print(f"     {axis}")
for i in range(3):
    pad = "." * (span - loads[i])
    print(f"M{i + 1}  |{rows[i]}{pad}| {loads[i]}")
total = sum(j[1] for j in jobs)
print(f"finish {span}, lower bound {(total + 2) // 3}")
