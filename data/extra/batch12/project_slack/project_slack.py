tasks = [("design", 5, []), ("order parts", 7, [0]), ("write code", 10, [0]), ("build rig", 4, [1]), ("test", 6, [2, 3]), ("manual", 3, [2]), ("ship", 2, [4, 5])]
n = len(tasks)
early = []
for name, days, after in tasks:
    s = 0
    for p in after:
        s = max(s, early[p] + tasks[p][1])
    early.append(s)
finish = 0
for i in range(n):
    finish = max(finish, early[i] + tasks[i][1])
lf = [finish] * n
j = n - 1
while j >= 0:
    ls = lf[j] - tasks[j][1]
    for p in tasks[j][2]:
        if ls < lf[p]:
            lf[p] = ls
    j -= 1
for k in range(n):
    name, days, after = tasks[k]
    slack = lf[k] - days - early[k]
    mark = " *" if slack == 0 else ""
    print(f"{name:<12} start day {early[k]:>2}, slack {slack}{mark}")
print(f"project takes {finish} days; * marks the critical path")
