def midi(note):
    letter = note[0]
    octave = int(note[-1])
    accidental = note[1:-1]
    base = ["C", "", "D", "", "E", "F", "", "G", "", "A", "", "B"].index(letter)
    shift = 1 if accidental == "#" else (-1 if accidental == "b" else 0)
    return (octave + 1) * 12 + base + shift

def simple_name(n):
    names = ["unison", "minor second", "major second", "minor third", "major third", "perfect fourth", "tritone", "perfect fifth", "minor sixth", "major sixth", "minor seventh", "major seventh"]
    return names[n % 12]

def describe(n):
    if n == 12:
        return "octave"
    if n > 12:
        return f"compound {simple_name(n)} ({n} semitones)"
    return simple_name(n)

pairs = [("C4", "G4"), ("E4", "C5"), ("A3", "C4"), ("F4", "B4"), ("D4", "D5"), ("C4", "E5"), ("Bb3", "Ab4"), ("G4", "F#5")]
for a, b in pairs:
    n = midi(b) - midi(a)
    inv = (12 - n % 12) % 12
    print(f"{a:<3} -> {b:<4} {describe(n)}, inverts to {simple_name(inv)}")
