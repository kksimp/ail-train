def analyse(notes):
    names = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
    shapes = [([0, 4, 7], ""), ([0, 3, 7], "m"), ([0, 3, 6], "dim"), ([0, 4, 7, 10], "7"), ([0, 3, 7, 10], "m7"), ([0, 4, 7, 11], "maj7"), ([0, 3, 6, 10], "m7b5")]
    triad_figs = ["5/3", "6", "6/4"]
    seventh_figs = ["7", "6/5", "4/3", "4/2"]
    inversions = ["root position", "first inversion", "second inversion", "third inversion"]
    pcs = []
    for n in notes:
        if n % 12 not in pcs:
            pcs.append(n % 12)
    for r in sorted(pcs):
        shape = sorted(set((p - r + 12) % 12 for p in pcs))
        for ivs, suffix in shapes:
            if ivs == shape:
                bass = (notes[0] % 12 - r + 12) % 12
                member = ivs.index(bass)
                figs = triad_figs[member] if len(ivs) == 3 else seventh_figs[member]
                return f"{names[r]}{suffix} {inversions[member]} ({figs})"
    return "unknown chord"

chords = [[48, 52, 55, 60], [52, 55, 60, 64], [43, 48, 52, 55], [43, 47, 50, 53], [47, 50, 53, 55], [50, 53, 55, 59], [41, 47, 50, 55], [45, 48, 52, 57], [50, 53, 59], [48, 53, 57, 62]]
for c in chords:
    shown = "[" + ", ".join(str(x) for x in c) + "]"
    print(f"{shown} {analyse(c)}")
