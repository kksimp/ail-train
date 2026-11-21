def relative_minor(key, sharp_side):
    sharps = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    flats = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    names = sharps if sharp_side else flats
    i = names.index(key) if key in names else 0
    return f"{names[(i + 9) % 12]}m"

sharp_keys = ["C", "G", "D", "A", "E", "B", "F#"]
flat_keys = ["F", "Bb", "Eb", "Ab", "Db", "Gb"]
sharp_order = ["F#", "C#", "G#", "D#", "A#", "E#", "B#"]
flat_order = ["Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"]
for n, k in enumerate(sharp_keys):
    acc = "no sharps or flats" if n == 0 else " ".join(sharp_order[0:n])
    print(f"{k:<3} {relative_minor(k, True):<4} {n} sharps: {acc}")
for i, k in enumerate(flat_keys):
    n = i + 1
    acc = " ".join(flat_order[0:n])
    print(f"{k:<3} {relative_minor(k, False):<4} {n} flats:  {acc}")
