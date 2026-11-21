NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def scale(root):
    out = [root]
    p = root
    for step in [2, 2, 1, 2, 2, 2]:
        p = (p + step) % 12
        out.append(p)
    return out

def triad_label(sc, degree):
    numerals = ["I", "II", "III", "IV", "V", "VI", "VII"]
    root = sc[degree]
    third = (sc[(degree + 2) % 7] - root + 12) % 12
    fifth = (sc[(degree + 4) % 7] - root + 12) % 12
    if third == 4:
        return numerals[degree]
    lower = numerals[degree].lower()
    return f"{lower}dim" if fifth == 6 else lower

def chord_name(sc, degree):
    label = triad_label(sc, degree)
    suffix = "dim" if label.endswith("dim") else ("m" if label == label.lower() else "")
    return f"{NAMES[sc[degree]]}{suffix}"

for key in ["C", "G", "E"]:
    sc = scale(NAMES.index(key))
    row = [f"{triad_label(sc, d)}={chord_name(sc, d)}" for d in range(7)]
    shown = " ".join(row)
    print(f"{key}: {shown}")
    prog = " ".join(chord_name(sc, d) for d in [0, 5, 3, 4])
    print(f"   I-vi-IV-V: {prog}")
