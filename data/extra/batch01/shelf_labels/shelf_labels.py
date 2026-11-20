def label(title, rows, width):
    inner = width - 2
    out = ["+" + "-" * inner + "+", "|" + title.upper().center(inner) + "|", "+" + "-" * inner + "+"]
    for name, qty in rows:
        q = str(qty)
        room = inner - len(q) - 2
        shown = name[:room - 1] + "~" if len(name) > room else name
        out.append("| " + shown.ljust(room, ".") + q + " |")
    out.append("+" + "-" * inner + "+")
    return out
for l in label("aisle 4", [("bolts M6", 120), ("washers", 8), ("extra long wood screws", 45)], 26):
    print(l)
for l in label("x", [("a", 1)], 9):
    print(l)
