def tones(name):
    roots = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    root = roots.get(name[0], 0)
    suffix = name[1:]
    shape = {"m": [0, 3, 7], "7": [0, 4, 7, 10], "m7": [0, 3, 7, 10], "maj7": [0, 4, 7, 11]}.get(suffix, [0, 4, 7])
    return [(root + i) % 12 for i in shape]

def finger(name):
    open_ = [40, 45, 50, 55, 59, 64]
    chord = tones(name)
    bass = False
    out = []
    for s in open_:
        pick = -1
        for f in range(5):
            p = (s + f) % 12
            if pick < 0 and ((bass and p in chord) or p == chord[0]):
                pick = f
        if pick >= 0:
            bass = True
            out.append(str(pick))
        else:
            out.append("x")
    return "".join(out)

for c in ["C", "G", "D", "Am", "Em", "E", "A7", "D7", "Cmaj7", "F"]:
    shape = finger(c)
    fretted = len([ch for ch in shape if ch != 'x' and ch != '0'])
    print(f"{c:<6} {shape}  ({fretted} fretted)")
