def pos(y):
    return ((y - 4) % 60 + 60) % 60
stems = ["Jia", "Yi", "Bing", "Ding", "Wu", "Ji", "Geng", "Xin", "Ren", "Gui"]
branches = ["Zi", "Chou", "Yin", "Mao", "Chen", "Si", "Wu", "Wei", "Shen", "You", "Xu", "Hai"]
animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
for y in [1949, 1966, 1984, 2000, 2024, 2026, 2044]:
    p = pos(y)
    print(f"{y}: {stems[p % 10]} {branches[p % 12]}, {elements[p % 10 // 2]} {animals[p % 12]}, year {p + 1} of the cycle")
for s, b in [[2, 6], [0, 1]]:
    years = [y for y in range(1950, 2050) if pos(y) % 10 == s and pos(y) % 12 == b]
    label = f"{stems[s]} {branches[b]}"
    if not years:
        print(f"{label} never occurs: stem and branch must share parity")
    else:
        print(f"{label} years in 1950..2049: [{', '.join(map(str, years))}]")
