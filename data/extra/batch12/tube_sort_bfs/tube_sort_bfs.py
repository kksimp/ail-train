def pour(tubes, a, b, cap):
    src = tubes[a]
    dst = tubes[b]
    if len(src) == 0 or len(dst) == cap:
        return []
    colour = src[-1]
    if len(dst) > 0 and dst[-1] != colour:
        return []
    run = 0
    k = len(src) - 1
    while k >= 0 and src[k] == colour:
        run += 1
        k -= 1
    amount = min(run, cap - len(dst))
    out = list(tubes)
    out[a] = tubes[a][0:len(src) - amount]
    out[b] = tubes[b] + colour * amount
    return out

def solved(tubes, cap):
    return all(len(t) == 0 or (len(t) == cap and all(c == t[0] for c in t)) for t in tubes)

start = ["RGB", "GBR", "BRG", "", ""]
cap = 3
key = "|".join(start)
came = {key: ""}
how = {key: ""}
queue = [start]
head = 0
goal = ""
while head < len(queue) and goal == "":
    cur = queue[head]
    head += 1
    if solved(cur, cap):
        goal = "|".join(cur)
    else:
        for a in range(len(cur)):
            for b in range(len(cur)):
                if a != b:
                    nxt = pour(cur, a, b, cap)
                    if len(nxt) > 0:
                        k = "|".join(nxt)
                        if k not in came:
                            came[k] = "|".join(cur)
                            how[k] = f"{a + 1}->{b + 1}"
                            queue.append(nxt)
steps = []
s = goal
while s != key:
    steps.append(f"{how[s]} giving {s}")
    s = came[s]
steps.reverse()
for line in steps:
    print(line)
print(f"{len(steps)} pours, {len(came)} states seen")
