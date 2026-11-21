def pitch(note):
    base = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    p = base.get(note[0], 0)
    if len(note) > 1 and note[1] == '#':
        p += 1
    elif len(note) > 1 and note[1] == 'b':
        p += 11
    return p % 12

def sing(tune, tonic):
    syllables = ["do", "di", "re", "ri", "mi", "fa", "fi", "sol", "si", "la", "li", "ti"]
    return " ".join(syllables[(pitch(n) - tonic + 12) % 12] for n in tune)

in_d = ["D", "D", "A", "A", "B", "B", "A", "G", "G", "F#", "F#", "E", "E", "D"]
in_f = ["F", "F", "C", "C", "D", "D", "C", "Bb", "Bb", "A", "A", "G", "G", "F"]
blues = ["C", "Eb", "F", "F#", "G", "Bb", "C"]
a = sing(in_d, pitch("D"))
b = sing(in_f, pitch("F"))
print(f"D major, movable: {a}")
print(f"F major, movable: {b}")
print(f"same syllables in both keys: {'true' if a == b else 'false'}")
print(f"D major, fixed do: {sing(in_d, 0)}")
print(f"C blues scale: {sing(blues, 0)}")
