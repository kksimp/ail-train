import heapq
names = ["Ann", "Bob", "Cat", "Dan"]
pace = [1, 2, 5, 10]
n = 4
states = 32
best = [1000000] * states
prev = [-1] * states
note = [""] * states
best[0] = 0
h = [0]
while h:
    v = heapq.heappop(h)
    t = v // 100
    s = v % 100
    if t > best[s]:
        continue
    far = (s >> 4) == 1
    people = s & 15
    for a in range(n):
        for b in range(a, n):
            on_side = people if far else 15 ^ people
            if ((on_side >> a) & 1) == 1 and ((on_side >> b) & 1) == 1:
                group = (1 << a) | (1 << b)
                moved = (people ^ group) | (0 if far else 16)
                cost = t + max(pace[a], pace[b])
                if cost < best[moved]:
                    best[moved] = cost
                    prev[moved] = s
                    who = names[a] if a == b else f"{names[a]}+{names[b]}"
                    d = "back" if far else "over"
                    note[moved] = f"{who} {d}"
                    heapq.heappush(h, cost * 100 + moved)
goal = 31
steps = []
s = goal
while s != 0:
    steps.append(f"{note[s]} (t={best[s]})")
    s = prev[s]
steps.reverse()
for line in steps:
    print(line)
print(f"everyone across in {best[goal]} minutes")
