def runs(line):
    small = {"a", "an", "the", "of", "and", "in", "on", "to"}
    out = []
    current = []
    letter = ' '
    for raw in line.split(" "):
        w = "".join(c for c in raw.lower() if c.isalpha())
        if w == "" or w in small:
            continue
        first = w[0]
        if first == letter:
            current.append(w)
        else:
            if len(current) >= 3:
                out.append(" ".join(current))
            current = [w]
            letter = first
    if len(current) >= 3:
        out.append(" ".join(current))
    return out

lines = ["Peter Piper picked a peck of pickled peppers", "She sells sea shells by the sea shore", "Big bad bears bring blue berries home", "The cat sat on the mat", "Silly snakes slide, then tiny turtles take the trail"]
for line in lines:
    rs = runs(line)
    shown = "no run" if not rs else " / ".join(rs)
    print(line)
    print(f"  -> {shown}")
