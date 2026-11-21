def fullest(queues, me):
    best = -1
    for w in range(len(queues)):
        if w != me and len(queues[w]) > 0 and (best < 0 or len(queues[w]) > len(queues[best])):
            best = w
    return best

start = [[5, 3, 8, 2, 4, 6, 3, 1], [2], []]
queues = [list(q) for q in start]
left = [0, 0, 0]
tick = 0
steals = 0
while any(q for q in queues) or any(x > 0 for x in left):
    for w in range(3):
        if left[w] == 0:
            if queues[w]:
                left[w] = queues[w].pop()
            else:
                v = fullest(queues, w)
                if v >= 0:
                    stolen = queues[v][0]
                    queues[v] = queues[v][1:]
                    left[w] = stolen
                    steals += 1
                    print(f"tick {tick:>2}: worker {w} steals a {stolen}-tick task from worker {v}")
        if left[w] > 0:
            left[w] -= 1
    tick += 1
no_steal = max(sum(q) for q in start)
print(f"all done after {tick} ticks with {steals} steals")
print(f"without stealing the first worker alone needs {no_steal} ticks")
