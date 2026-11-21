def second_digit(first, second, third):
    if first in "AEIOU":
        table = {'b': 2, 'd': 3, 'l': 4, 'm': 4, 'n': 5, 'p': 6, 'r': 7, 's': 8, 't': 8, 'u': 9, 'v': 9, 'w': 9, 'x': 9, 'y': 9}
        return table.get(second, 2)
    if first == 'S':
        if second == 'c' and third == 'h':
            return 3
        table = {'a': 2, 'e': 4, 'h': 5, 'i': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 6, 't': 7, 'u': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}
        return table.get(second, 2)
    table = {'a': 3, 'e': 4, 'i': 5, 'o': 6, 'r': 7, 'u': 8, 'y': 9}
    return table.get(second, 2)

def third_digit(c):
    if 'a' <= c <= 'd':
        return 3
    if 'e' <= c <= 'h':
        return 4
    if 'i' <= c <= 'l':
        return 5
    if 'm' <= c <= 'o':
        return 6
    if 'p' <= c <= 's':
        return 7
    if 't' <= c <= 'v':
        return 8
    return 9

def cutter(name):
    n2 = second_digit(name[0], name[1], name[2])
    n3 = third_digit(name[2])
    return f".{name[0]}{n2}{n3}"

authors = ["Adams", "Ellison", "Ondaatje", "Smith", "Schmidt", "Sterne", "Campbell", "Ceccarelli", "Tolkien", "Morrison", "Woolf", "Brontë", "Austen", "Hughes"]
seen = {}
for a in authors:
    c = cutter(a)
    clash = seen.get(c, "")
    note = "" if clash == "" else f" (same as {clash}, add a further digit)"
    if clash == "":
        seen[c] = a
    print(f"{a:<11} {c}{note}")
order = sorted(authors, key=lambda a: cutter(a))
print(f"shelf order: {', '.join(order)}")
