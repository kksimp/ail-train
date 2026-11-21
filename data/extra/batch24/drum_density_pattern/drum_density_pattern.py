state = 2718
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def weight(step): return 4 if step % 4 == 0 else 2 if step % 2 == 0 else 1
def chance(voice, step):
    w = weight(step)
    if voice == 0: return 100 if step == 0 else 20 * w
    if voice == 1: return 100 if step % 8 == 4 else 5 * w
    return 40 + 15 * w
voices = ["kick ", "snare", "hat  "]
hits = [0, 0, 0]
for bar in range(1, 3):
    for v in range(3):
        line = []
        for step in range(16):
            if below(100) < chance(v, step):
                line.append('x'); hits[v] += 1
            else: line.append('.')
        print(f"bar {bar} {voices[v]} {''.join(line)}")
print(f"hits: kick {hits[0]}, snare {hits[1]}, hat {hits[2]}")
