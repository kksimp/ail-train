state = 88
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def name(i): return f"{'CDEFGAB'[i % 7]}{4 + i // 7}"
def nearest_c(i): return i - i % 7 if i % 7 <= 3 else i - i % 7 + 7
moves = [-2, -1, -1, 1, 1, 2, 3, -3, 0]
note = 7; tune = [note]; owe = 0
for k in range(14):
    step = moves[below(len(moves))]
    if owe != 0:
        step = owe; owe = 0
    elif step > 2 or step < -2:
        owe = -1 if step > 0 else 1
    note = min(max(note + step, 0), 14)
    tune.append(note)
tune.append(nearest_c(note))
named = [name(t) for t in tune]
print(" ".join(named[:8]))
print(" ".join(named[8:]))
print(f"range {name(min(tune))} to {name(max(tune))}, {len(tune)} notes")
