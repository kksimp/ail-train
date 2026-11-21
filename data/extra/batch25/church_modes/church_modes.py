def pc(note):
    base = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    p = base.get(note[0], 0)
    if len(note) > 1:
        p += 1 if note[1] == '#' else 11
    return p % 12

def mode_scale(final, m):
    steps = [2, 2, 1, 2, 2, 2, 1]
    s = set()
    p = final
    for i in range(7):
        s.add(p)
        p = (p + steps[(m + i) % 7]) % 12
    return s

modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
tunes = ["D F E D G A B A D", "E F G E D C D E", "F A C B A G F", "G B D F E D G", "A C E D C B A", "D F# A G F# E D", "G Bb D C Bb A G E F G", "B D F E D C B"]
for t in tunes:
    notes = t.split(" ")
    final = pc(notes[-1])
    used = set(pc(n) for n in notes)
    fits = [modes[m] for m in range(7) if used <= mode_scale(final, m)]
    last = notes[-1]
    print(f"{t:<22} final {last:<2} {' or '.join(fits)}")
