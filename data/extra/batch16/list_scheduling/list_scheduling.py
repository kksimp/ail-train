def prio(i, lat, deps, memo):
    if memo[i] >= 0:
        return memo[i]
    best = 0
    for j in range(len(deps)):
        if i in deps[j]:
            best = max(best, prio(j, lat, deps, memo))
    memo[i] = lat[i] + best
    return memo[i]

def ready(i, cycle, deps, lat, issue):
    return all(issue[d] >= 0 and issue[d] + lat[d] <= cycle for d in deps[i])

def schedule(names, lat, deps, by_rank):
    n = len(names)
    memo = [-1] * n
    issue = [-1] * n
    order = []
    cycle = 0
    done = 0
    while done < n:
        pick = -1
        for i in range(n):
            if issue[i] < 0 and ready(i, cycle, deps, lat, issue):
                if pick < 0 or (by_rank and prio(i, lat, deps, memo) > prio(pick, lat, deps, memo)):
                    pick = i
            if not by_rank and issue[i] < 0:
                break
        if pick >= 0:
            issue[pick] = cycle
            order.append(f"{cycle}:{names[pick]}")
            done += 1
        cycle += 1
    finish = 0
    for i in range(n):
        finish = max(finish, issue[i] + lat[i])
    print(" ".join(order))
    return finish

names = ["ldA", "ldB", "mul", "ldC", "add", "ldD", "sub", "st"]
lat = [3, 3, 2, 3, 1, 3, 1, 1]
deps = [[], [], [0, 1], [], [2, 3], [], [5], [4, 6]]
print("in order:")
a = schedule(names, lat, deps, False)
print(f"finishes at cycle {a}")
print("critical path first:")
b = schedule(names, lat, deps, True)
print(f"finishes at cycle {b}, saving {a - b} cycles")
