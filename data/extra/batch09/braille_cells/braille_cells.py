def dots(c):
    base = ["1", "12", "14", "145", "15", "124", "1245", "125", "24", "245"]
    i = ord(c) - 97
    if c == 'w':
        s = "2456"
    elif i < 10:
        s = base[i]
    elif i < 20:
        s = base[i - 10] + "3"
    else:
        k = i - 21 if i > 22 else i - 20
        s = base[k] + "36"
    return [int(d) for d in s]

def render(word):
    rows = []
    for r in range(3):
        cells = []
        for c in word:
            ds = dots(c)
            left = "o" if (r + 1) in ds else "."
            right = "o" if (r + 4) in ds else "."
            cells.append(left + right)
        rows.append(" ".join(cells))
    return rows

for word in ["hello", "braille", "quiz"]:
    names = "-".join("".join(str(d) for d in sorted(dots(c))) for c in word)
    print(f"{word}: {names}")
    for row in render(word):
        print(f"  {row}")
