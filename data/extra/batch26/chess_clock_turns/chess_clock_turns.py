w = b = 180; inc = 2; turn = "White"
mss = lambda s: f"{s // 60}:{s % 60:02}"
for i, used in enumerate([12, 30, 25, 41, 60, 18, 95, 22]):
    mover = turn
    if turn == "White":
        w -= used
        if w < 0:
            print(f"move {i + 1}: {mover} used {used} s and lost on time"); break
        w += inc; turn = "Black"
    else:
        b -= used
        if b < 0:
            print(f"move {i + 1}: {mover} used {used} s and lost on time"); break
        b += inc; turn = "White"
    print(f"move {i + 1}: {mover} {used} s, clocks {mss(w)} | {mss(b)}")
print(f"turn now: {turn}")
