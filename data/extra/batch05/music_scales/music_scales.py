N = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def sc(r, st):
    i = N.index(r); o = [N[i]]
    for s in st: i = (i + s) % 12; o.append(N[i])
    return o
for r in ["C", "G", "D", "A#"]:
    print(f"{r} major: {' '.join(sc(r, [2, 2, 1, 2, 2, 2, 1]))}"); print(f"{r} minor: {' '.join(sc(r, [2, 1, 2, 2, 1, 2, 2]))}")
