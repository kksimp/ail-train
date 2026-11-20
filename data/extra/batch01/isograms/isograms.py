def first_repeat(w):
    seen = set()
    for c in w.lower():
        if c in " -":
            continue
        if c in seen:
            return c
        seen.add(c)
    return None
for w in ["lumberjacks", "background", "six-year-old", "Alphabet", "isograms", "Emily Jung Schwartzkopf", ""]:
    c = first_repeat(w)
    print(f"'{w}': repeats '{c}'" if c else f"'{w}': isogram")
s = "subdermatoglyphic"
print(f"{len(s)} letters, {len(set(s))} distinct")
