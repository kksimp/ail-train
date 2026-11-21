R = ["CATSX", "OWLNE", "DOGAT", "EMUTN", "BEARS"]
D = [(0, 1, "E"), (1, 0, "S"), (1, 1, "SE"), (-1, 1, "NE"), (0, -1, "W"), (-1, 0, "N"), (-1, -1, "NW"), (1, -1, "SW")]
def fw(w):
    for r in range(5):
        for c in range(5):
            for dr, dc, n in D:
                if all(0 <= r + dr * i < 5 and 0 <= c + dc * i < 5 and R[r + dr * i][c + dc * i] == w[i] for i in range(len(w))): return f"({r}, {c}) going {n}"
    return "not found"
for w in ["CAT", "OWL", "DOG", "BEAR", "TAG", "CODE", "NET", "EMU", "LION"]: print(f"{w:<5} {fw(w)}")
