tasks = [("fetch", 4, []), ("codegen", 2, [0]), ("lib", 9, [0]), ("proto", 3, [1]), ("server", 5, [2, 3]), ("cli", 2, [3]), ("tests", 6, [4, 5]), ("docs", 1, [1])]
n = len(tasks)
wave = []
finish = []
for i in range(n):
    w = 0
    ready = 0
    for d in tasks[i][2]:
        w = max(w, wave[d] + 1)
        ready = max(ready, finish[d])
    wave.append(w)
    finish.append(ready + tasks[i][1])
top = max(wave)
wave_total = 0
for w in range(top + 1):
    members = [i for i in range(n) if wave[i] == w]
    slowest = max(tasks[i][1] for i in members)
    wave_total += slowest
    names = ", ".join(tasks[i][0] for i in members)
    print(f"wave {w}: {names} (slowest {slowest}s)")
serial = sum(t[1] for t in tasks)
critical = max(finish)
print(f"one at a time: {serial}s")
print(f"wave by wave:  {wave_total}s")
print(f"critical path: {critical}s")
