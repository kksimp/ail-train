def symbols(d):
    sizes = [16, 12, 8, 6, 4, 3, 2, 1]
    marks = ["w", "h.", "h", "q.", "q", "e.", "e", "s"]
    left = d
    out = []
    for i, s in enumerate(sizes):
        while left >= s:
            out.append(marks[i])
            left -= s
    return out

def bars(notes, bar):
    out = []
    current = []
    room = bar
    for n in notes:
        left = n
        while left > 0:
            piece = min(left, room)
            for s in symbols(piece):
                current.append(s)
            left -= piece
            room -= piece
            if left > 0:
                current[-1] = f"{current[-1]}~"
            if room == 0:
                out.append(" ".join(current))
                current = []
                room = bar
    if current:
        out.append(f"{' '.join(current)} (rest {room})")
    return f"| {' | '.join(out)} |"

tune = [4, 4, 6, 2, 8, 12, 4, 2, 2, 8, 6, 2]
print(f"4/4: {bars(tune, 16)}")
print(f"3/4: {bars(tune, 12)}")
waltz = [8, 4, 6, 6, 4, 12, 3, 1, 8]
print(f"6/8: {bars(waltz, 12)}")
