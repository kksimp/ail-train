state = 0
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def allowed(a, b): return abs(a - b) <= 1
def fill(strip, backs):
    if len(strip) == 12: return strip[11] == 0
    last = strip[-1]
    start = below(4)
    for k in range(4):
        t = (start + k) % 4
        if allowed(last, t):
            strip.append(t)
            if fill(strip, backs): return True
            strip.pop()
            backs[0] += 1
    return False
marks = "~:\"^"
for seed in [3, 33, 333]:
    state = seed
    strip = [3]; backs = [0]
    if fill(strip, backs):
        print(f"seed {seed:>3}: {''.join(marks[t] for t in strip)}  ({backs[0]} backtracks)")
print("key: ~ water, : sand, \" grass, ^ rock; every strip starts on rock")
