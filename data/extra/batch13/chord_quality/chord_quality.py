def pitch(note):
    base = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9}.get(note[0], 11)
    shift = 1 if note.endswith("#") else (-1 if note.endswith("b") else 0)
    return (base + shift + 12) % 12

Q = {"4 7": "major", "3 7": "minor", "3 6": "diminished", "4 8": "augmented", "2 7": "suspended second", "5 7": "suspended fourth", "4 7 10": "dominant seventh", "4 7 11": "major seventh", "3 7 10": "minor seventh", "3 6 10": "half-diminished seventh", "3 6 9": "diminished seventh"}

def quality(steps):
    return Q.get(" ".join(str(s) for s in steps), "")

def name(chord):
    notes = chord.split(" ")
    for r, root in enumerate(notes):
        p = pitch(root)
        steps = set()
        for n in notes:
            if n != root:
                steps.add((pitch(n) - p + 12) % 12)
        q = quality(sorted(steps))
        if q != "":
            inv = "" if r == 0 else f" (inversion, {notes[0]} in the bass)"
            return f"{root} {q}{inv}"
    return "unknown"

for chord in ["C E G", "A C E", "G B D F", "E G Bb", "F A C E", "E G C", "D F A C", "C F G", "B D F Ab", "C E G#", "C D Eb"]:
    print(f"{chord:<9} {name(chord)}")
