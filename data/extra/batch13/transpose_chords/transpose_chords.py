SHARPS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FLATS = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

def split_root(sym):
    n = 2 if len(sym) > 1 and sym[1] in "#b" else 1
    return [sym[0:n], sym[n:]]

def move_note(note, by, flat):
    i = SHARPS.index(note) if note in SHARPS else (FLATS.index(note) if note in FLATS else 0)
    j = ((i + by) % 12 + 12) % 12
    return FLATS[j] if flat else SHARPS[j]

def transpose(chord, by, flat):
    halves = chord.split("/")
    parts = split_root(halves[0])
    top = f"{move_note(parts[0], by, flat)}{parts[1]}"
    if len(halves) == 2:
        return f"{top}/{move_note(halves[1], by, flat)}"
    return top

song = ["C", "Am7", "F", "G7", "Bb", "D/F#", "Gsus4", "C"]
flat_keys = ["F", "Bb", "Eb", "Ab", "Db"]
print(f"in C: {' '.join(song)}")
for by in [2, -2, 5, 3, -5]:
    key = move_note("C", by, True)
    flat = key in flat_keys
    shown = " ".join(transpose(c, by, flat) for c in song)
    new_key = move_note("C", by, flat)
    print(f"in {new_key:<2} ({by:>2}): {shown}")
