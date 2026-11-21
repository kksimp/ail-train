state = 5
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def tick_once(ph):
    n = len(ph)
    flashed = []; queue = []
    for i in range(n):
        ph[i] += 1
        flashed.append(ph[i] >= 100)
        if ph[i] >= 100: queue.append(i)
    while queue:
        k = queue.pop(0)
        ph[k] = 0
        for j in [(k + n - 1) % n, (k + 1) % n]:
            if not flashed[j]:
                ph[j] += 15
                if ph[j] >= 100:
                    flashed[j] = True; queue.append(j)
    return any(flashed)
ph = [below(100) for i in range(8)]
print(f"start phases {ph}")
for w in range(8):
    flash_ticks = 0
    for t in range(100):
        if tick_once(ph): flash_ticks += 1
    print(f"ticks {w * 100:>3}-{w * 100 + 99:>3}: flashes on {flash_ticks} separate ticks")
print(f"end phases {ph}")
